import os
import django
import re

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.apps import apps
from django.contrib.gis.db import models as gis_models

app_name = 'buildings'  # Replace with your app name
models_list = [model for model in apps.get_app_config(app_name).get_models()]

# Generate serializers.py content
serializers_content = """from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (\n    """

serializers_content += ",\n    ".join(model.__name__ for model in models_list)
serializers_content += "\n)\n\n"

for model in models_list:
    # Check if model has geometric fields
    geo_fields = [field.name for field in model._meta.get_fields() 
                if isinstance(field, gis_models.GeometryField)]
    
    if geo_fields:
        geo_field = geo_fields[0]
        serializers_content += f"""class {model.__name__}Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = {model.__name__}
        geo_field = '{geo_field}'
        fields = '__all__'

"""
    else:
        serializers_content += f"""class {model.__name__}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model.__name__}
        fields = '__all__'

"""

# Generate api_views.py content
api_views_content = """from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter
from .models import (\n    """

api_views_content += ",\n    ".join(model.__name__ for model in models_list)
api_views_content += "\n)\n"

api_views_content += """from .serializers import (\n    """
api_views_content += "Serializer,\n    ".join(model.__name__ for model in models_list)
api_views_content += "Serializer\n)\n\n"

for model in models_list:
    # Check if model has geometric fields
    geo_fields = [field.name for field in model._meta.get_fields() 
                if isinstance(field, gis_models.GeometryField)]
    
    # Determine search fields
    search_fields = []
    for field in model._meta.get_fields():
        if hasattr(field, 'get_internal_type'):
            field_type = field.get_internal_type()
            if field_type in ['CharField', 'TextField'] and not field.name.endswith('_field'):
                search_fields.append(field.name)
    
    # Limited filterset fields to common field names
    common_filter_fields = ['quartier', 'arrondisse', 'commune', 'country', 'nom', 'name']
    model_filter_fields = []
    for field in model._meta.get_fields():
        if hasattr(field, 'name') and field.name in common_filter_fields:
            model_filter_fields.append(field.name)
    
    filter_fields_str = ", ".join(f"'{field}'" for field in model_filter_fields)
    search_fields_str = ", ".join(f"'{field}'" for field in search_fields)
    
    if geo_fields:
        geo_field = geo_fields[0]
        api_views_content += f"""class {model.__name__}ViewSet(viewsets.ModelViewSet):
    \"""
    API endpoint for {model.__name__}.
    \"""
    queryset = {model.__name__}.objects.all()
    serializer_class = {model.__name__}Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = [{filter_fields_str}]
    search_fields = [{search_fields_str}]
    bbox_filter_field = '{geo_field}'
    distance_filter_field = '{geo_field}'
    bbox_filter_include_overlapping = True

"""
    else:
        api_views_content += f"""class {model.__name__}ViewSet(viewsets.ModelViewSet):
    \"""
    API endpoint for {model.__name__}.
    \"""
    queryset = {model.__name__}.objects.all()
    serializer_class = {model.__name__}Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [{filter_fields_str}]
    search_fields = [{search_fields_str}]

"""

# Generate urls.py content
urls_content = """from django.urls import include, path
from rest_framework import routers
from .api_views import (\n    """

urls_content += "ViewSet,\n    ".join(model.__name__ for model in models_list)
urls_content += "ViewSet\n)\n\n"

urls_content += """router = routers.DefaultRouter()\n"""

for model in models_list:
    # Create a slug for the URL
    model_name = model.__name__
    # First convert CamelCase to separate words
    url_name = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', model_name).lower()
    # Remove common suffixes
    url_name = url_name.replace('-point', '')
    url_name = url_name.replace('-region', '')
    url_name = url_name.replace('-polyline', '')
    # Convert spaces to dashes and make lowercase
    url_name = '-'.join(url_name.split()).lower()
    
    urls_content += f"""router.register(r'{url_name}', {model.__name__}ViewSet)\n"""

urls_content += """\nurlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
"""

# Write files
with open(f'{app_name}/serializers.py', 'w') as f:
    f.write(serializers_content)

with open(f'{app_name}/api_views.py', 'w') as f:
    f.write(api_views_content)

with open(f'{app_name}/urls_api.py', 'w') as f:
    f.write(urls_content)

print("Files generated successfully!")