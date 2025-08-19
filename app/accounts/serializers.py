from accounts.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers as _serializers


class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # expose an 'identifier' field that can be username or email
        self.fields['identifier'] = _serializers.CharField(required=False, write_only=True)
        # make the configured username field optional so clients can send 'identifier' instead
        username_field = self.username_field if hasattr(self, 'username_field') else 'username'
        if username_field in self.fields:
            self.fields[username_field].required = False

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token
        token['email'] = user.email
        token['username'] = user.username

        return token
    

    def validate(self, attrs):
        # Accept an 'identifier' field which can be either the username or the email.
        # If provided, try to resolve it to the actual username and inject it into attrs
        # so the parent TokenObtainPairSerializer can authenticate normally.
        username_field = self.username_field if hasattr(self, 'username_field') else 'username'

        if not attrs.get(username_field):
            identifier = attrs.get('identifier') or attrs.get('email')
            if identifier:
                try:
                    # prefer exact username match, then email
                    user = (
                        User.objects.filter(username__iexact=identifier).first()
                        or User.objects.filter(email__iexact=identifier).first()
                    )
                    if user:
                        attrs[username_field] = user.get_username()
                except Exception:
                    # fallback: leave attrs unchanged and let parent raise
                    pass

        # Call parent validation (this performs the actual authentication)
        data = super().validate(attrs)

        # Add extra response data
        # data['email'] = getattr(self.user, 'email', None)
        # data['user_id'] = getattr(self.user, 'id', None)
        # data['username'] = getattr(self.user, 'username', None)
        data['user'] = UserSerializer(self.user).data

        return data




class UserSerializer(serializers.ModelSerializer):
   
    class Meta:

        model = User
        fields = ["id","username","email",
                  "password", "is_superuser", "role"]
        
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "is_superuser" : {
                "read_only": True
            },
            "role" : {
                "read_only": True
            }
        }
    
    def create(self, validated_data, *args, **kwargs):
      
        user = self.Meta.model.objects.create_user(**validated_data)
        
        return user


class AdminSerializer(UserSerializer):
    def create(self, validated_data, *args, **kwargs):
        user = self.Meta.model.objects.create_superuser(**validated_data)
        return user


class StoredRefreshTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('accounts.models', fromlist=['StoredRefreshToken']).StoredRefreshToken
        fields = ['id', 'user', 'jti', 'ip_address', 'user_agent', 'created_at', 'expires_at', 'revoked']
        read_only_fields = ['created_at']
    
