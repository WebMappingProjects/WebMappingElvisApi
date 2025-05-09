from accounts.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token
        token['email'] = user.email
        token['username'] = user.username

        return token
    

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra response data
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        data['username'] = self.user.username


        return data




class UserSerializer(serializers.ModelSerializer):
   
    class Meta:

        model = User
        fields = ["id","username","email",
                  "password", "is_superuser"]
        
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "is_superuser" : {
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
    
