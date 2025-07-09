from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.gis.geos import Point, Polygon
from django.contrib.gis.measure import D
from django.db.models import Q, Count, Sum
from buildings.models import (
    Region, Departement, Commune, Conseiller, Route, Hydrographie,
    Sante, CentreSante, Pharmacie, Enseignement, Eglise, Securite,
    Hebergement, ServicePublique, Projet
)
from buildings.new_serializers import (
    RegionSerializer, RegionDetailSerializer, DepartementSerializer, DepartementDetailSerializer,
    CommuneSerializer, CommuneDetailSerializer, ConseillerSerializer, RouteSerializer,
    HydrographieSerializer, SanteSerializer, CentreSanteSerializer, PharmacieSerializer,
    EnseignementSerializer, EgliseSerializer, SecuriteSerializer, HebergementSerializer,
    ServicePubliqueSerializer, ProjetSerializer,
    StatisticsSerializer, SearchSerializer
)

from accounts.permissions import *





class BaseGISViewSet(viewsets.ModelViewSet):
    """Base ViewSet for GIS models with common spatial operations"""
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [TechnicienOrReadOnly]
    
    @action(detail=False, methods=['post'])
    def within_bbox(self, request):
        """Get features within a bounding box"""
        try:
            bbox = request.data.get('bbox')  # [min_lon, min_lat, max_lon, max_lat]
            if not bbox or len(bbox) != 4:
                return Response({'error': 'Invalid bbox format'}, status=status.HTTP_400_BAD_REQUEST)
            
            polygon = Polygon.from_bbox(bbox)
            queryset = self.get_queryset().filter(geom__within=polygon)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def intersects(self, request):
        """Get features that intersect with given geometry"""
        try:
            geom_data = request.data.get('geometry')
            if not geom_data:
                return Response({'error': 'Geometry required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Assuming GeoJSON format
            from django.contrib.gis.geos import GEOSGeometry
            geometry = GEOSGeometry(str(geom_data))
            queryset = self.get_queryset().filter(geom__intersects=geometry)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def within_distance(self, request):
        """Get features within distance of a point"""
        try:
            lat = float(request.data.get('lat'))
            lon = float(request.data.get('lon'))
            distance = float(request.data.get('distance', 1000))  # meters
            
            point = Point(lon, lat, srid=4326)
            queryset = self.get_queryset().filter(geom__distance_lte=(point, D(m=distance)))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except (ValueError, TypeError) as e:
            return Response({'error': 'Invalid coordinates or distance'}, status=status.HTTP_400_BAD_REQUEST)


class RegionViewSet(BaseGISViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    search_fields = ['nom']
    ordering_fields = ['nom', 'superficie']
    ordering = ['nom']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RegionDetailSerializer
        return RegionSerializer
    
    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        """Get statistics for a specific region"""
        region = self.get_object()
        stats = {
            'departements_count': region.departements.count(),
            'communes_count': Commune.objects.filter(departement__region=region).count(),
            'superficie_totale': region.superficie,
            'conseillers_count': region.conseillers.count(),
            'services': {
                'sante': Sante.objects.filter(commune__departement__region=region).count(),
                'enseignement': Enseignement.objects.filter(commune__departement__region=region).count(),
                'eglises': Eglise.objects.filter(commune__departement__region=region).count(),
                'securite': Securite.objects.filter(commune__departement__region=region).count(),
                'hebergements': Hebergement.objects.filter(commune__departement__region=region).count(),
            }
        }
        return Response(stats)


class DepartementViewSet(BaseGISViewSet):
    queryset = Departement.objects.select_related('region').all()
    serializer_class = DepartementSerializer
    search_fields = ['nom', 'region__nom']
    filterset_fields = ['region']
    ordering_fields = ['nom', 'superficie']
    ordering = ['nom']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DepartementDetailSerializer
        return DepartementSerializer
    
    @action(detail=True, methods=['get'])
    def communes_by_superficie(self, request, pk=None):
        """Get communes ordered by superficie"""
        departement = self.get_object()
        communes = departement.communes.order_by('-superficie')
        serializer = CommuneSerializer(communes, many=True)
        return Response(serializer.data)


class CommuneViewSet(BaseGISViewSet):
    queryset = Commune.objects.select_related('departement__region').all()
    serializer_class = CommuneSerializer
    search_fields = ['nom', 'maire', 'departement__nom']
    filterset_fields = ['departement', 'departement__region']
    ordering_fields = ['nom', 'superficie']
    ordering = ['nom']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommuneDetailSerializer
        return CommuneSerializer
    
    @action(detail=True, methods=['get'])
    def services_summary(self, request, pk=None):
        """Get summary of all services in the commune"""
        commune = self.get_object()
        summary = {
            'routes': {
                'count': commune.routes.count(),
                'total_longueur': commune.routes.aggregate(Sum('longueur'))['longueur__sum'] or 0,
                'by_type': commune.routes.values('type').annotate(count=Count('id'))
            },
            'sante': {
                'centres': commune.services_sante.filter(centresante__isnull=False).count(),
                'pharmacies': commune.services_sante.filter(pharmacie__isnull=False).count()
            },
            'enseignement': {
                'count': commune.etablissements_enseignement.count(),
                'total_effectif': commune.etablissements_enseignement.aggregate(Sum('effectif'))['effectif__sum'] or 0,
                'by_level': commune.etablissements_enseignement.values('enseignement').annotate(count=Count('id'))
            },
            'projets': {
                'count': commune.projets.count(),
                'total_montant': commune.projets.aggregate(Sum('montant'))['montant__sum'] or 0,
                'en_cours': commune.projets.filter(date_livraison__gte=timezone.now().date()).count()
            }
        }
        return Response(summary)


class ConseillerViewSet(viewsets.ModelViewSet):
    queryset = Conseiller.objects.select_related('region').all()
    serializer_class = ConseillerSerializer
    permission_classes = [TechnicienOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom', 'role', 'region__nom']
    filterset_fields = ['region', 'role']
    ordering_fields = ['nom', 'fin_mandat']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def expiring_mandates(self, request):
        """Get councillors with mandates expiring soon"""
        from datetime import datetime, timedelta
        expiry_date = datetime.now().date() + timedelta(days=90)  # 3 months
        expiring = self.get_queryset().filter(fin_mandat__lte=expiry_date)
        serializer = self.get_serializer(expiring, many=True)
        return Response(serializer.data)


class RouteViewSet(BaseGISViewSet):
    queryset = Route.objects.select_related('region').all()
    serializer_class = RouteSerializer
    search_fields = ['nom', 'region__nom']
    filterset_fields = ['type', 'region']
    ordering_fields = ['nom', 'longueur']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def by_type_statistics(self, request):
        """Get route statistics by type"""
        stats = self.get_queryset().values('type').annotate(
            count=Count('id'),
            total_longueur=Sum('longueur')
        ).order_by('type')
        return Response(stats)


class HydrographieViewSet(BaseGISViewSet):
    queryset = Hydrographie.objects.select_related('region').all()
    serializer_class = HydrographieSerializer
    search_fields = ['nom', 'region__nom']
    # filterset_fields = ['commune', 'commune__departement']
    filterset_fields = ['region']
    ordering_fields = ['nom', 'longueur']
    ordering = ['nom']


class SanteViewSet(BaseGISViewSet):
    queryset = Sante.objects.select_related('commune').all()
    serializer_class = SanteSerializer
    search_fields = ['nom', 'commune__nom']
    filterset_fields = ['commune', 'commune__departement']
    ordering_fields = ['nom']
    ordering = ['nom']


class CentreSanteViewSet(BaseGISViewSet):
    queryset = CentreSante.objects.select_related('commune').all()
    serializer_class = CentreSanteSerializer
    search_fields = ['nom', 'commune__nom']
    filterset_fields = ['type', 'commune', 'commune__departement']
    ordering_fields = ['nom']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get health centers grouped by type"""
        stats = self.get_queryset().values('type').annotate(count=Count('id'))
        return Response(stats)


class PharmacieViewSet(BaseGISViewSet):
    queryset = Pharmacie.objects.select_related('commune').all()
    serializer_class = PharmacieSerializer
    search_fields = ['nom', 'nom_pharmacien', 'commune__nom']
    filterset_fields = ['commune', 'commune__departement']
    ordering_fields = ['nom', 'nom_pharmacien']
    ordering = ['nom']


class EnseignementViewSet(BaseGISViewSet):
    queryset = Enseignement.objects.select_related('commune').all()
    serializer_class = EnseignementSerializer
    search_fields = ['nom', 'nom_responsable', 'commune__nom']
    filterset_fields = ['type', 'religion', 'enseignement', 'formation', 'commune']
    ordering_fields = ['nom', 'effectif']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get education statistics"""
        stats = {
            'by_type': self.get_queryset().values('type').annotate(
                count=Count('id'),
                total_effectif=Sum('effectif')
            ),
            'by_level': self.get_queryset().values('enseignement').annotate(
                count=Count('id'),
                total_effectif=Sum('effectif')
            ),
            'by_religion': self.get_queryset().values('religion').annotate(count=Count('id')),
            'total_effectif': self.get_queryset().aggregate(Sum('effectif'))['effectif__sum'] or 0
        }
        return Response(stats)


class EgliseViewSet(BaseGISViewSet):
    queryset = Eglise.objects.select_related('commune').all()
    serializer_class = EgliseSerializer
    search_fields = ['nom', 'commune__nom']
    filterset_fields = ['type', 'structure', 'commune', 'commune__departement']
    ordering_fields = ['nom', 'capacite']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def capacity_statistics(self, request):
        """Get church capacity statistics"""
        stats = {
            'total_capacity': self.get_queryset().aggregate(Sum('capacite'))['capacite__sum'] or 0,
            'by_type': self.get_queryset().values('type').annotate(
                count=Count('id'),
                total_capacity=Sum('capacite')
            ),
            'by_structure': self.get_queryset().values('structure').annotate(count=Count('id'))
        }
        return Response(stats)


class SecuriteViewSet(BaseGISViewSet):
    queryset = Securite.objects.select_related('commune').all()
    serializer_class = SecuriteSerializer
    search_fields = ['nom', 'commune__nom']
    filterset_fields = ['type', 'commune', 'commune__departement']
    ordering_fields = ['nom', 'nombre_agent']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def agent_statistics(self, request):
        """Get security agent statistics"""
        stats = {
            'total_agents': self.get_queryset().aggregate(Sum('nombre_agent'))['nombre_agent__sum'] or 0,
            'by_type': self.get_queryset().values('type').annotate(
                count=Count('id'),
                total_agents=Sum('nombre_agent')
            )
        }
        return Response(stats)


class HebergementViewSet(BaseGISViewSet):
    queryset = Hebergement.objects.select_related('commune').all()
    serializer_class = HebergementSerializer
    search_fields = ['nom', 'standing', 'commune__nom']
    filterset_fields = ['type', 'commune', 'commune__departement']
    ordering_fields = ['nom', 'nb_chambres']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def accommodation_stats(self, request):
        """Get accommodation statistics"""
        stats = {
            'total_chambres': self.get_queryset().aggregate(Sum('nb_chambres'))['nb_chambres__sum'] or 0,
            'by_type': self.get_queryset().values('type').annotate(
                count=Count('id'),
                total_chambres=Sum('nb_chambres')
            ),
            'by_standing': self.get_queryset().values('standing').annotate(count=Count('id'))
        }
        return Response(stats)


class ServicePubliqueViewSet(BaseGISViewSet):
    queryset = ServicePublique.objects.select_related('commune').all()
    serializer_class = ServicePubliqueSerializer
    search_fields = ['nom', 'commune__nom']
    filterset_fields = ['type', 'commune', 'commune__departement']
    ordering_fields = ['nom']
    ordering = ['nom']
    
    @action(detail=False, methods=['get'])
    def by_type_count(self, request):
        """Get public services count by type"""
        stats = self.get_queryset().values('type').annotate(count=Count('id'))
        return Response(stats)


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.select_related('commune').all()
    serializer_class = ProjetSerializer
    permission_classes = [TechnicienOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom_contractant', 'description', 'commune__nom']
    filterset_fields = ['service', 'commune', 'commune__departement']
    ordering_fields = ['date_debut', 'date_livraison', 'montant']
    ordering = ['-date_debut']
    
    @action(detail=False, methods=['get'])
    def ongoing(self, request):
        """Get ongoing projects"""
        from django.utils import timezone
        ongoing = self.get_queryset().filter(
            date_debut__lte=timezone.now().date(),
            date_livraison__gte=timezone.now().date()
        )
        serializer = self.get_serializer(ongoing, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Get completed projects"""
        from django.utils import timezone
        completed = self.get_queryset().filter(date_livraison__lt=timezone.now().date())
        serializer = self.get_serializer(completed, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def budget_statistics(self, request):
        """Get project budget statistics"""
        from django.utils import timezone
        current_date = timezone.now().date()
        
        stats = {
            'total_budget': self.get_queryset().aggregate(Sum('montant'))['montant__sum'] or 0,
            'ongoing_budget': self.get_queryset().filter(
                date_debut__lte=current_date,
                date_livraison__gte=current_date
            ).aggregate(Sum('montant'))['montant__sum'] or 0,
            'completed_budget': self.get_queryset().filter(
                date_livraison__lt=current_date
            ).aggregate(Sum('montant'))['montant__sum'] or 0,
            'by_service': self.get_queryset().values('service').annotate(
                count=Count('id'),
                total_budget=Sum('montant')
            )
        }
        return Response(stats)



# Global API ViewSet for dashboard statistics
class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [TechnicienOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def global_statistics(self, request):
        """Get global dashboard statistics"""
        stats = {
            'regions_count': Region.objects.count(),
            'departements_count': Departement.objects.count(),
            'communes_count': Commune.objects.count(),
            'total_superficie': Region.objects.aggregate(Sum('superficie'))['superficie__sum'] or 0,
            'services_count': {
                'sante': Sante.objects.count(),
                'enseignement': Enseignement.objects.count(),
                'eglises': Eglise.objects.count(),
                'securite': Securite.objects.count(),
                'hebergements': Hebergement.objects.count(),
                'services_publiques': ServicePublique.objects.count(),
            },
            'projets_count': Projet.objects.count(),
            'total_montant_projets': Projet.objects.aggregate(Sum('montant'))['montant__sum'] or 0,
            'routes_total_km': Route.objects.aggregate(Sum('longueur'))['longueur__sum'] or 0,
            'total_effectif_scolaire': Enseignement.objects.aggregate(Sum('effectif'))['effectif__sum'] or 0
        }
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def search(self, request):
        """Global search across all entities"""
        serializer = SearchSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        query = serializer.validated_data['query']
        search_type = serializer.validated_data.get('type')
        commune_id = serializer.validated_data.get('commune')
        departement_id = serializer.validated_data.get('departement')
        region_id = serializer.validated_data.get('region')
        
        results = {}
        
        # Build base filters
        base_filters = Q()
        if commune_id:
            base_filters &= Q(commune_id=commune_id)
        elif departement_id:
            base_filters &= Q(commune__departement_id=departement_id)
        elif region_id:
            base_filters &= Q(commune__departement__region_id=region_id)
        
        # Search in different models based on type or search all
        if not search_type or search_type == 'region':
            regions = Region.objects.filter(nom__icontains=query)
            if region_id:
                regions = regions.filter(id=region_id)
            results['regions'] = RegionSerializer(regions[:10], many=True).data
        
        if not search_type or search_type == 'commune':
            commune_filters = Q(nom__icontains=query) | Q(maire__icontains=query)
            if departement_id:
                commune_filters &= Q(departement_id=departement_id)
            elif region_id:
                commune_filters &= Q(departement__region_id=region_id)
            communes = Commune.objects.filter(commune_filters)
            results['communes'] = CommuneSerializer(communes[:10], many=True).data
        
        if not search_type or search_type == 'sante':
            sante_filters = Q(nom__icontains=query) & base_filters
            sante = Sante.objects.filter(sante_filters)
            results['sante'] = SanteSerializer(sante[:10], many=True).data
        
        # Add more search types as needed...
        
        return Response(results)