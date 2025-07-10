from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from accounts.models import User
from buildings.models import (
    Region, Departement, Commune, Conseiller, Route, Hydrographie,
    Sante, CentreSante, Pharmacie, Enseignement, Eglise, Securite,
    Hebergement, ServicePublique, Projet
)




# Base Geographic Serializers
class RegionSerializer(GeoFeatureModelSerializer):
    departements_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Region
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'departements_count']
    
    def get_departements_count(self, obj):
        return obj.departements.count()


class DepartementSerializer(GeoFeatureModelSerializer):
    region_nom = serializers.CharField(source='region.nom', read_only=True)
    communes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Departement
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'region', 'region_nom', 'communes_count']
    
    def get_communes_count(self, obj):
        return obj.communes.count()


class ConseillerSerializer(serializers.ModelSerializer):
    region_nom = serializers.CharField(source='region.nom', read_only=True)
    
    class Meta:
        model = Conseiller
        fields = ['id', 'nom', 'telephone', 'fin_mandat', 'role', 'region', 'region_nom']


class CommuneSerializer(GeoFeatureModelSerializer):
    departement_nom = serializers.CharField(source='departement.nom', read_only=True)
    region_nom = serializers.CharField(source='departement.region.nom', read_only=True)
    services_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Commune
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'maire', 'departement', 'departement_nom', 
                 'region_nom', 'services_count']
    
    def get_services_count(self, obj):
        return {
            # 'routes': obj.routes.count(),
            'sante': obj.services_sante.count(),
            'enseignement': obj.etablissements_enseignement.count(),
            'eglises': obj.eglises.count(),
            'securite': obj.services_securite.count(),
            'hebergements': obj.hebergements.count(),
            'services_publiques': obj.services_publiques.count(),
            'projets': obj.projets.count()
        }


# Infrastructure Serializers
class RouteSerializer(GeoFeatureModelSerializer):
    region_nom = serializers.CharField(source='region.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = Route
        geo_field = 'geom'
        fields = ['id', 'nom', 'longueur', 'type', 'type_display', 'region', 'region_nom']


class HydrographieSerializer(GeoFeatureModelSerializer):
    region_nom = serializers.CharField(source='region.nom', read_only=True)
    
    class Meta:
        model = Hydrographie
        geo_field = 'geom'
        fields = ['id', 'nom', 'longueur', 'region', 'region_nom']


# Services Serializers
class SanteSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    
    class Meta:
        model = Sante
        geo_field = 'geom'
        fields = ['id', 'nom', 'commune', 'commune_nom']


class CentreSanteSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = CentreSante
        geo_field = 'geom'
        fields = ['id', 'nom', 'type', 'type_display', 'commune', 'commune_nom']


class PharmacieSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    
    class Meta:
        model = Pharmacie
        geo_field = 'geom'
        fields = ['id', 'nom', 'nom_pharmacien', 'commune', 'commune_nom']


class EnseignementSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    religion_display = serializers.CharField(source='get_religion_display', read_only=True)
    enseignement_display = serializers.CharField(source='get_enseignement_display', read_only=True)
    formation_display = serializers.CharField(source='get_formation_display', read_only=True)
    
    class Meta:
        model = Enseignement
        geo_field = 'geom'
        fields = ['id', 'nom', 'nom_responsable', 'effectif', 'type', 'type_display',
                 'religion', 'religion_display', 'enseignement', 'enseignement_display',
                 'formation', 'formation_display', 'meilleur_diplome', 'commune', 'commune_nom']


class EgliseSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    structure_display = serializers.CharField(source='get_structure_display', read_only=True)
    
    class Meta:
        model = Eglise
        geo_field = 'geom'
        fields = ['id', 'nom', 'capacite', 'type', 'type_display', 'structure', 
                 'structure_display', 'commune', 'commune_nom']


class SecuriteSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = Securite
        geo_field = 'geom'
        fields = ['id', 'nom', 'nombre_agent', 'type', 'type_display', 'commune', 'commune_nom']


class HebergementSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = Hebergement
        geo_field = 'geom'
        fields = ['id', 'nom', 'nb_chambres', 'type', 'type_display', 'standing', 
                 'commune', 'commune_nom']


class ServicePubliqueSerializer(GeoFeatureModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = ServicePublique
        geo_field = 'geom'
        fields = ['id', 'nom', 'type', 'type_display', 'commune', 'commune_nom']


class ProjetSerializer(serializers.ModelSerializer):
    commune_nom = serializers.CharField(source='commune.nom', read_only=True)
    service_display = serializers.CharField(source='get_service_display', read_only=True)
    duree_projet = serializers.SerializerMethodField()
    
    class Meta:
        model = Projet
        fields = ['id', 'nom_contractant', 'description', 'montant', 'date_debut',
                 'date_livraison', 'service', 'service_display', 'commune', 'commune_nom',
                 'duree_projet']
    
    def get_duree_projet(self, obj):
        return (obj.date_livraison - obj.date_debut).days


class UtilisateurSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(source='get_role_display', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 
                 'role_display', 'is_active', 'date_joined']
        read_only_fields = ['date_joined']


# Nested Serializers for detailed views
class RegionDetailSerializer(GeoFeatureModelSerializer):
    departements = DepartementSerializer(many=True, read_only=True)
    conseillers = ConseillerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Region
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'departements', 'conseillers']


class DepartementDetailSerializer(GeoFeatureModelSerializer):
    region = RegionSerializer(read_only=True)
    communes = CommuneSerializer(many=True, read_only=True)
    
    class Meta:
        model = Departement
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'region', 'communes']


class CommuneDetailSerializer(GeoFeatureModelSerializer):
    departement = DepartementSerializer(read_only=True)
    #routes = RouteSerializer(many=True, read_only=True)
    services_sante = SanteSerializer(many=True, read_only=True)
    etablissements_enseignement = EnseignementSerializer(many=True, read_only=True)
    eglises = EgliseSerializer(many=True, read_only=True)
    services_securite = SecuriteSerializer(many=True, read_only=True)
    hebergements = HebergementSerializer(many=True, read_only=True)
    services_publiques = ServicePubliqueSerializer(many=True, read_only=True)
    projets = ProjetSerializer(many=True, read_only=True)
    
    class Meta:
        model = Commune
        geo_field = 'geom'
        fields = ['id', 'nom', 'superficie', 'maire', 'departement',
                 'services_sante', 'etablissements_enseignement', 'eglises',
                 'services_securite', 'hebergements', 'services_publiques', 'projets']


# Statistics Serializers
class StatisticsSerializer(serializers.Serializer):
    regions_count = serializers.IntegerField()
    departements_count = serializers.IntegerField()
    communes_count = serializers.IntegerField()
    total_superficie = serializers.DecimalField(max_digits=20, decimal_places=2)
    services_count = serializers.DictField()
    projets_count = serializers.IntegerField()
    total_montant_projets = serializers.IntegerField()


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=[
        'region', 'departement', 'commune', 'route', 'sante', 
        'enseignement', 'eglise', 'securite', 'hebergement', 'service_publique'
    ], required=False)
    commune = serializers.IntegerField(required=False)
    departement = serializers.IntegerField(required=False)
    region = serializers.IntegerField(required=False)