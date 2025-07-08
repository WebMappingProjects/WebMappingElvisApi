from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets as views
from buildings.new_views import (
    ServiceStatisticsView,
    GroupedDataView,
    AverageDistanceView,
    NearestServiceView
)
# Create a router and register our viewsets with it
router = DefaultRouter()

# Geographic entities
router.register(r'regions', views.RegionViewSet)
router.register(r'departements', views.DepartementViewSet)
router.register(r'communes', views.CommuneViewSet)
router.register(r'conseillers', views.ConseillerViewSet)

# Infrastructure
router.register(r'routes', views.RouteViewSet)
router.register(r'hydrographie', views.HydrographieViewSet)

# Services
router.register(r'sante', views.SanteViewSet)
router.register(r'centres-sante', views.CentreSanteViewSet)
router.register(r'pharmacies', views.PharmacieViewSet)
router.register(r'enseignement', views.EnseignementViewSet)
router.register(r'eglises', views.EgliseViewSet)
router.register(r'securite', views.SecuriteViewSet)
router.register(r'hebergements', views.HebergementViewSet)
router.register(r'services-publiques', views.ServicePubliqueViewSet)

# Projects
router.register(r'projets', views.ProjetViewSet)

# Dashboard
router.register(r'dashboard', views.DashboardViewSet, basename='dashboard')

# The API URLs are now determined automatically by the router
urlpatterns = router.urls

urlpatterns += [
    path('count/', ServiceStatisticsView.as_view(), name='service-statistics'),
    path('group/', GroupedDataView.as_view(), name='grouped-data'),
    path('distance/', AverageDistanceView.as_view(), name='average-distance'),
    path('nearest/', NearestServiceView.as_view(), name='nearest-service'),
]