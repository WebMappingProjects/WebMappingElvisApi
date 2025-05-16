from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter
from .models import (
    AfricaRegion,
    AgencesDeVoyagesFontPoint,
    AmbassadesPoint,
    ArmeeFontPoint,
    ArrondAireMetrop,
    AubergesCustomPoint,
    AxesVoiriesPolyline,
    BacsFontPoint,
    BacsPoint,
    BanquesEtMicrofinancesCustomPoint,
    BassinVersantMfoundiBasRegion,
    BassinVersantMfoundiRegion,
    BassinVersantNone,
    BassinVersantRegion,
    BatiDurPolyline,
    BatiLocauxPolyline,
    BatiPublicsPoint,
    BatiPublicsRegion,
    BatimentsYaoundePoint,
    BatimentsYaoundePolyline,
    BatimentsYaoundeRegion,
    BouchesIncendiesYdeCustomPoint,
    BouchesIncendiesYdePoint,
    BoulangeriesCustomPoint,
    BoulangeriesRegion,
    CampSicCustomPoint,
    CentreSpecialDetatCivilFontPoint,
    CentresCulturelsCustomPoint,
    CimetiereRegion,
    CinemaCustomPoint,
    CitesMunicipalesCuyPoint,
    CommissariatsYdeFontPoint,
    ComplexesSportifsCustomPoint,
    ConsulatsPoint,
    DelegationsCustomPoint,
    DepAireMetrop,
    EcoleNormaleDesInstituteursDenseignementGeneralPoint,
    EcolesMatPrimairePoint,
    EglisesCatholiquesFontPoint,
    EglisesPresbyteriennesFontPoint,
    EglisesProtestantesPoint,
    EnseignementDeBaseFontPoint,
    EnseignementMaternelleCustomPoint,
    EnseignementMaternelleRegion,
    EnseignementPrimaireFontPoint,
    EnseignementPrimaireRegion,
    EnseignementSuperieurCustomPoint,
    EnseignementsSecondairesFinalPoint,
    EspaceVertEllipse,
    EspaceVertRegion,
    EspacesAmenagesRegion,
    EtalonnagePolyline,
    FeuTricoloreCustomPoint,
    FeuTricoloreEllipse,
    FeuTricolorePolyline,
    FeuTricoloreRegion,
    GaragesCustomPoint,
    GareFerroviaireCustomPoint,
    GaresRoutieresCuyPoint,
    GendarmeriesPoint,
    HangarsPolyline,
    HotelsFontPoint,
    HussiersYdeCustomPoint,
    ItinerairePrcPolyline,
    LacHorsCartoRegion,
    LacRegion,
    LaveriesFontPoint,
    Layer,
    LeMfoundiPolyline,
    LieuxRemarquablesCustomPoint,
    LieuxRemarquablesFontPoint,
    LieuxRemarquablesPoint,
    LigneBusPolyline,
    LigneBusProjetPolyline,
    LimiteMokoloPolyline,
    LimiteYde,
    LimiteYde1Region,
    LimitesDesCommunesYdeRegion,
    MairiesYaoundeCustomPoint,
    MarcheEligedzoaRegion,
    MarcheEligedzoaZoneActiviteRegion,
    MarcheMokoloRegion,
    MarchesCommunauxCuyPoint,
    MarchesCuyPoint,
    MarchesPoint,
    MarchesRegion,
    MinisteresYaoundeCustomPoint,
    MonumentsEllipse,
    MonumentsRegion,
    MosqueesFontPoint,
    MursPolyline,
    NationsUniesPoint,
    ParkingsCuy2007Polyline,
    ParkingsCuyPolyline,
    PharmaciesPoint,
    PrefecturesSousPrefecturesCustomPoint,
    ProjetsRouteEllipse,
    ProjetsRoutePolyline,
    QuadrillageNone,
    QuadrillagePoint,
    QuadrillageRegion,
    QuartierRegion,
    QuartiersPoint,
    RadioYaoundeCustomPoint,
    ReligionsYaoundeFontPoint,
    ReligionsYaoundePoint,
    ReseauEpPolyline,
    RestaurantsYaoundeFontPoint,
    RivieresPolyline,
    RivieresRegion,
    RouteEnProjetPolyline,
    SanitaireYaoundePoint,
    SapeursPompierPoint,
    ServicesCuyPoint,
    StationsSevicesFontPoint,
    SupZoneUrbaRegion,
    TerrainsDeSportsCustomPoint,
    ToilettesPubliquesCuyPoint,
    Topology,
    VoieFerreePolyline,
    VoiriesYaoundePoint,
    VoiriesYaoundePolyline,
    WorldFontPoint,
    WorldPolyline,
    WorldRegion,
    Z1C121CPolyline,
    Z1C122CPoint,
    Z1C122CPolyline,
    Z1C131CPolyline,
    Z1C132CPolyline,
    Z1C133CPolyline,
    ZoneAdressageRegion,
    ZonesProscritesEllipse
)
from .serializers import (
    AfricaRegionSerializer,
    AgencesDeVoyagesFontPointSerializer,
    AmbassadesPointSerializer,
    ArmeeFontPointSerializer,
    ArrondAireMetropSerializer,
    AubergesCustomPointSerializer,
    AxesVoiriesPolylineSerializer,
    BacsFontPointSerializer,
    BacsPointSerializer,
    BanquesEtMicrofinancesCustomPointSerializer,
    BassinVersantMfoundiBasRegionSerializer,
    BassinVersantMfoundiRegionSerializer,
    BassinVersantNoneSerializer,
    BassinVersantRegionSerializer,
    BatiDurPolylineSerializer,
    BatiLocauxPolylineSerializer,
    BatiPublicsPointSerializer,
    BatiPublicsRegionSerializer,
    BatimentsYaoundePointSerializer,
    BatimentsYaoundePolylineSerializer,
    BatimentsYaoundeRegionSerializer,
    BouchesIncendiesYdeCustomPointSerializer,
    BouchesIncendiesYdePointSerializer,
    BoulangeriesCustomPointSerializer,
    BoulangeriesRegionSerializer,
    CampSicCustomPointSerializer,
    CentreSpecialDetatCivilFontPointSerializer,
    CentresCulturelsCustomPointSerializer,
    CimetiereRegionSerializer,
    CinemaCustomPointSerializer,
    CitesMunicipalesCuyPointSerializer,
    CommissariatsYdeFontPointSerializer,
    ComplexesSportifsCustomPointSerializer,
    ConsulatsPointSerializer,
    DelegationsCustomPointSerializer,
    DepAireMetropSerializer,
    EcoleNormaleDesInstituteursDenseignementGeneralPointSerializer,
    EcolesMatPrimairePointSerializer,
    EglisesCatholiquesFontPointSerializer,
    EglisesPresbyteriennesFontPointSerializer,
    EglisesProtestantesPointSerializer,
    EnseignementDeBaseFontPointSerializer,
    EnseignementMaternelleCustomPointSerializer,
    EnseignementMaternelleRegionSerializer,
    EnseignementPrimaireFontPointSerializer,
    EnseignementPrimaireRegionSerializer,
    EnseignementSuperieurCustomPointSerializer,
    EnseignementsSecondairesFinalPointSerializer,
    EspaceVertEllipseSerializer,
    EspaceVertRegionSerializer,
    EspacesAmenagesRegionSerializer,
    EtalonnagePolylineSerializer,
    FeuTricoloreCustomPointSerializer,
    FeuTricoloreEllipseSerializer,
    FeuTricolorePolylineSerializer,
    FeuTricoloreRegionSerializer,
    GaragesCustomPointSerializer,
    GareFerroviaireCustomPointSerializer,
    GaresRoutieresCuyPointSerializer,
    GendarmeriesPointSerializer,
    HangarsPolylineSerializer,
    HotelsFontPointSerializer,
    HussiersYdeCustomPointSerializer,
    ItinerairePrcPolylineSerializer,
    LacHorsCartoRegionSerializer,
    LacRegionSerializer,
    LaveriesFontPointSerializer,
    LayerSerializer,
    LeMfoundiPolylineSerializer,
    LieuxRemarquablesCustomPointSerializer,
    LieuxRemarquablesFontPointSerializer,
    LieuxRemarquablesPointSerializer,
    LigneBusPolylineSerializer,
    LigneBusProjetPolylineSerializer,
    LimiteMokoloPolylineSerializer,
    LimiteYdeSerializer,
    LimiteYde1RegionSerializer,
    LimitesDesCommunesYdeRegionSerializer,
    MairiesYaoundeCustomPointSerializer,
    MarcheEligedzoaRegionSerializer,
    MarcheEligedzoaZoneActiviteRegionSerializer,
    MarcheMokoloRegionSerializer,
    MarchesCommunauxCuyPointSerializer,
    MarchesCuyPointSerializer,
    MarchesPointSerializer,
    MarchesRegionSerializer,
    MinisteresYaoundeCustomPointSerializer,
    MonumentsEllipseSerializer,
    MonumentsRegionSerializer,
    MosqueesFontPointSerializer,
    MursPolylineSerializer,
    NationsUniesPointSerializer,
    ParkingsCuy2007PolylineSerializer,
    ParkingsCuyPolylineSerializer,
    PharmaciesPointSerializer,
    PrefecturesSousPrefecturesCustomPointSerializer,
    ProjetsRouteEllipseSerializer,
    ProjetsRoutePolylineSerializer,
    QuadrillageNoneSerializer,
    QuadrillagePointSerializer,
    QuadrillageRegionSerializer,
    QuartierRegionSerializer,
    QuartiersPointSerializer,
    RadioYaoundeCustomPointSerializer,
    ReligionsYaoundeFontPointSerializer,
    ReligionsYaoundePointSerializer,
    ReseauEpPolylineSerializer,
    RestaurantsYaoundeFontPointSerializer,
    RivieresPolylineSerializer,
    RivieresRegionSerializer,
    RouteEnProjetPolylineSerializer,
    SanitaireYaoundePointSerializer,
    SapeursPompierPointSerializer,
    ServicesCuyPointSerializer,
    StationsSevicesFontPointSerializer,
    SupZoneUrbaRegionSerializer,
    TerrainsDeSportsCustomPointSerializer,
    ToilettesPubliquesCuyPointSerializer,
    TopologySerializer,
    VoieFerreePolylineSerializer,
    VoiriesYaoundePointSerializer,
    VoiriesYaoundePolylineSerializer,
    WorldFontPointSerializer,
    WorldPolylineSerializer,
    WorldRegionSerializer,
    Z1C121CPolylineSerializer,
    Z1C122CPointSerializer,
    Z1C122CPolylineSerializer,
    Z1C131CPolylineSerializer,
    Z1C132CPolylineSerializer,
    Z1C133CPolylineSerializer,
    ZoneAdressageRegionSerializer,
    ZonesProscritesEllipseSerializer
)

class AfricaRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for AfricaRegion.
    """
    queryset = AfricaRegion.objects.all()
    serializer_class = AfricaRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['country']
    search_fields = ['country', 'capital', 'continent', 'fips', 'iso_2', 'iso_3']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class AgencesDeVoyagesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for AgencesDeVoyagesFontPoint.
    """
    queryset = AgencesDeVoyagesFontPoint.objects.all()
    serializer_class = AgencesDeVoyagesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class AmbassadesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for AmbassadesPoint.
    """
    queryset = AmbassadesPoint.objects.all()
    serializer_class = AmbassadesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'longitude', 'latitude', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ArmeeFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ArmeeFontPoint.
    """
    queryset = ArmeeFontPoint.objects.all()
    serializer_class = ArmeeFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'type', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ArrondAireMetropViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ArrondAireMetrop.
    """
    queryset = ArrondAireMetrop.objects.all()
    serializer_class = ArrondAireMetropSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['province', 'departemen', 'codedepart', 'arrond', 'codearrond', 'arr_minatd', 'cir_ad', 'resultat', 'responsabl']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class AubergesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for AubergesCustomPoint.
    """
    queryset = AubergesCustomPoint.objects.all()
    serializer_class = AubergesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class AxesVoiriesPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for AxesVoiriesPolyline.
    """
    queryset = AxesVoiriesPolyline.objects.all()
    serializer_class = AxesVoiriesPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['hierarchie', 'nomrue', 'type_axe', 'etat']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BacsFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BacsFontPoint.
    """
    queryset = BacsFontPoint.objects.all()
    serializer_class = BacsFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['code', 'position', 'capacite']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BacsPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BacsPoint.
    """
    queryset = BacsPoint.objects.all()
    serializer_class = BacsPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['code', 'position', 'capacite']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BanquesEtMicrofinancesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BanquesEtMicrofinancesCustomPoint.
    """
    queryset = BanquesEtMicrofinancesCustomPoint.objects.all()
    serializer_class = BanquesEtMicrofinancesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'type', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BassinVersantMfoundiBasRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BassinVersantMfoundiBasRegion.
    """
    queryset = BassinVersantMfoundiBasRegion.objects.all()
    serializer_class = BassinVersantMfoundiBasRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['n_bv', 'cours_bv']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BassinVersantMfoundiRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BassinVersantMfoundiRegion.
    """
    queryset = BassinVersantMfoundiRegion.objects.all()
    serializer_class = BassinVersantMfoundiRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['nom_bassin']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BassinVersantNoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BassinVersantNone.
    """
    queryset = BassinVersantNone.objects.all()
    serializer_class = BassinVersantNoneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['n_bv', 'cours_bv']

class BassinVersantRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BassinVersantRegion.
    """
    queryset = BassinVersantRegion.objects.all()
    serializer_class = BassinVersantRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['n_bv', 'cours_bv']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatiDurPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatiDurPolyline.
    """
    queryset = BatiDurPolyline.objects.all()
    serializer_class = BatiDurPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatiLocauxPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatiLocauxPolyline.
    """
    queryset = BatiLocauxPolyline.objects.all()
    serializer_class = BatiLocauxPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatiPublicsPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatiPublicsPoint.
    """
    queryset = BatiPublicsPoint.objects.all()
    serializer_class = BatiPublicsPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatiPublicsRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatiPublicsRegion.
    """
    queryset = BatiPublicsRegion.objects.all()
    serializer_class = BatiPublicsRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatimentsYaoundePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatimentsYaoundePoint.
    """
    queryset = BatimentsYaoundePoint.objects.all()
    serializer_class = BatimentsYaoundePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatimentsYaoundePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatimentsYaoundePolyline.
    """
    queryset = BatimentsYaoundePolyline.objects.all()
    serializer_class = BatimentsYaoundePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BatimentsYaoundeRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BatimentsYaoundeRegion.
    """
    queryset = BatimentsYaoundeRegion.objects.all()
    serializer_class = BatimentsYaoundeRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BouchesIncendiesYdeCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BouchesIncendiesYdeCustomPoint.
    """
    queryset = BouchesIncendiesYdeCustomPoint.objects.all()
    serializer_class = BouchesIncendiesYdeCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['matricule', 'symbole']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BouchesIncendiesYdePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BouchesIncendiesYdePoint.
    """
    queryset = BouchesIncendiesYdePoint.objects.all()
    serializer_class = BouchesIncendiesYdePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['matricule', 'symbole']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BoulangeriesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BoulangeriesCustomPoint.
    """
    queryset = BoulangeriesCustomPoint.objects.all()
    serializer_class = BoulangeriesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse', 'standing', 'propri_tai']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class BoulangeriesRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for BoulangeriesRegion.
    """
    queryset = BoulangeriesRegion.objects.all()
    serializer_class = BoulangeriesRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse', 'standing', 'propri_tai']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CampSicCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CampSicCustomPoint.
    """
    queryset = CampSicCustomPoint.objects.all()
    serializer_class = CampSicCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CentreSpecialDetatCivilFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CentreSpecialDetatCivilFontPoint.
    """
    queryset = CentreSpecialDetatCivilFontPoint.objects.all()
    serializer_class = CentreSpecialDetatCivilFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CentresCulturelsCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CentresCulturelsCustomPoint.
    """
    queryset = CentresCulturelsCustomPoint.objects.all()
    serializer_class = CentresCulturelsCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'commune']
    search_fields = ['nom', 'quartier', 'promoteur', 'e_mail', 'offerts', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CimetiereRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CimetiereRegion.
    """
    queryset = CimetiereRegion.objects.all()
    serializer_class = CimetiereRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['cimeti_re', 'localisati', 'arrondiss']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CinemaCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CinemaCustomPoint.
    """
    queryset = CinemaCustomPoint.objects.all()
    serializer_class = CinemaCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'commune']
    search_fields = ['nom', 'promoteur', 'e_mail', 'offerts', 'quartier', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CitesMunicipalesCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CitesMunicipalesCuyPoint.
    """
    queryset = CitesMunicipalesCuyPoint.objects.all()
    serializer_class = CitesMunicipalesCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class CommissariatsYdeFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CommissariatsYdeFontPoint.
    """
    queryset = CommissariatsYdeFontPoint.objects.all()
    serializer_class = CommissariatsYdeFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'localisati', 'contact', 'commissari', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ComplexesSportifsCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ComplexesSportifsCustomPoint.
    """
    queryset = ComplexesSportifsCustomPoint.objects.all()
    serializer_class = ComplexesSportifsCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'commune']
    search_fields = ['noms', 'type', 'quartier', 'discipline', 'commune', 'standing']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ConsulatsPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ConsulatsPoint.
    """
    queryset = ConsulatsPoint.objects.all()
    serializer_class = ConsulatsPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'postale', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class DelegationsCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for DelegationsCustomPoint.
    """
    queryset = DelegationsCustomPoint.objects.all()
    serializer_class = DelegationsCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class DepAireMetropViewSet(viewsets.ModelViewSet):
    """
    API endpoint for DepAireMetrop.
    """
    queryset = DepAireMetrop.objects.all()
    serializer_class = DepAireMetropSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['minatd', 'code_prov', 'departemen', 'départemen', 'province', 'chef_lieu']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EcoleNormaleDesInstituteursDenseignementGeneralPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EcoleNormaleDesInstituteursDenseignementGeneralPoint.
    """
    queryset = EcoleNormaleDesInstituteursDenseignementGeneralPoint.objects.all()
    serializer_class = EcoleNormaleDesInstituteursDenseignementGeneralPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['numero', 'nom', 'localisati', 'contact', 'telephone', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EcolesMatPrimairePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EcolesMatPrimairePoint.
    """
    queryset = EcolesMatPrimairePoint.objects.all()
    serializer_class = EcolesMatPrimairePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['code_ecole', 'nom', 'telephone', 'bp', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EglisesCatholiquesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EglisesCatholiquesFontPoint.
    """
    queryset = EglisesCatholiquesFontPoint.objects.all()
    serializer_class = EglisesCatholiquesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'postale', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EglisesPresbyteriennesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EglisesPresbyteriennesFontPoint.
    """
    queryset = EglisesPresbyteriennesFontPoint.objects.all()
    serializer_class = EglisesPresbyteriennesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'postale', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EglisesProtestantesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EglisesProtestantesPoint.
    """
    queryset = EglisesProtestantesPoint.objects.all()
    serializer_class = EglisesProtestantesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephonne', 'postale', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementDeBaseFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementDeBaseFontPoint.
    """
    queryset = EnseignementDeBaseFontPoint.objects.all()
    serializer_class = EnseignementDeBaseFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'telephone', 'bp', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementMaternelleCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementMaternelleCustomPoint.
    """
    queryset = EnseignementMaternelleCustomPoint.objects.all()
    serializer_class = EnseignementMaternelleCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'arrondisse']
    search_fields = ['ecoles', 'telephone', 'postale', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementMaternelleRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementMaternelleRegion.
    """
    queryset = EnseignementMaternelleRegion.objects.all()
    serializer_class = EnseignementMaternelleRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'arrondisse']
    search_fields = ['ecoles', 'telephone', 'postale', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementPrimaireFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementPrimaireFontPoint.
    """
    queryset = EnseignementPrimaireFontPoint.objects.all()
    serializer_class = EnseignementPrimaireFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['numero', 'publics', 'quartier0', 'tel_phone', 'bp', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementPrimaireRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementPrimaireRegion.
    """
    queryset = EnseignementPrimaireRegion.objects.all()
    serializer_class = EnseignementPrimaireRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['numero', 'publics', 'quartier0', 'tel_phone', 'bp', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementSuperieurCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementSuperieurCustomPoint.
    """
    queryset = EnseignementSuperieurCustomPoint.objects.all()
    serializer_class = EnseignementSuperieurCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'contact', 'telephone', 'fax', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EnseignementsSecondairesFinalPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EnseignementsSecondairesFinalPoint.
    """
    queryset = EnseignementsSecondairesFinalPoint.objects.all()
    serializer_class = EnseignementsSecondairesFinalPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['etablissem', 'localisati', 'fondateur', 'contact', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EspaceVertEllipseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EspaceVertEllipse.
    """
    queryset = EspaceVertEllipse.objects.all()
    serializer_class = EspaceVertEllipseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['commune']
    search_fields = ['code', 'espace', 'denominati', 'etat', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EspaceVertRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EspaceVertRegion.
    """
    queryset = EspaceVertRegion.objects.all()
    serializer_class = EspaceVertRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['commune']
    search_fields = ['code', 'espace', 'denominati', 'etat', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EspacesAmenagesRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EspacesAmenagesRegion.
    """
    queryset = EspacesAmenagesRegion.objects.all()
    serializer_class = EspacesAmenagesRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['lieu', 'creation']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class EtalonnagePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for EtalonnagePolyline.
    """
    queryset = EtalonnagePolyline.objects.all()
    serializer_class = EtalonnagePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class FeuTricoloreCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for FeuTricoloreCustomPoint.
    """
    queryset = FeuTricoloreCustomPoint.objects.all()
    serializer_class = FeuTricoloreCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['non']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class FeuTricoloreEllipseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for FeuTricoloreEllipse.
    """
    queryset = FeuTricoloreEllipse.objects.all()
    serializer_class = FeuTricoloreEllipseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['non']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class FeuTricolorePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for FeuTricolorePolyline.
    """
    queryset = FeuTricolorePolyline.objects.all()
    serializer_class = FeuTricolorePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['non']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class FeuTricoloreRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for FeuTricoloreRegion.
    """
    queryset = FeuTricoloreRegion.objects.all()
    serializer_class = FeuTricoloreRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['non']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class GaragesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for GaragesCustomPoint.
    """
    queryset = GaragesCustomPoint.objects.all()
    serializer_class = GaragesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 't_l_phone', 'postale', 'quartier', 'standing']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class GareFerroviaireCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for GareFerroviaireCustomPoint.
    """
    queryset = GareFerroviaireCustomPoint.objects.all()
    serializer_class = GareFerroviaireCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'sup', 'actualisee', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class GaresRoutieresCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for GaresRoutieresCuyPoint.
    """
    queryset = GaresRoutieresCuyPoint.objects.all()
    serializer_class = GaresRoutieresCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'sup', 'actualisee', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class GendarmeriesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for GendarmeriesPoint.
    """
    queryset = GendarmeriesPoint.objects.all()
    serializer_class = GendarmeriesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['d_nominati', 'bo_te_post', 'num_ro_t_l', 'sp_cialisa', 'localisati']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class HangarsPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for HangarsPolyline.
    """
    queryset = HangarsPolyline.objects.all()
    serializer_class = HangarsPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class HotelsFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for HotelsFontPoint.
    """
    queryset = HotelsFontPoint.objects.all()
    serializer_class = HotelsFontPointSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    # filterset_fields = ['quartier', 'commune']
    # search_fields = ['nom_h_tel', 'postale', 'telephone', 'quartier', 'commune', 'standing']
    # bbox_filter_field = 'geom'
    # distance_filter_field = 'geom'
    # bbox_filter_include_overlapping = True

class HussiersYdeCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for HussiersYdeCustomPoint.
    """
    queryset = HussiersYdeCustomPoint.objects.all()
    serializer_class = HussiersYdeCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'charge', 'localisati', 't_l_phone', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ItinerairePrcPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ItinerairePrcPolyline.
    """
    queryset = ItinerairePrcPolyline.objects.all()
    serializer_class = ItinerairePrcPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['it', 'lineaire', 'etat']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LacHorsCartoRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LacHorsCartoRegion.
    """
    queryset = LacHorsCartoRegion.objects.all()
    serializer_class = LacHorsCartoRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LacRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LacRegion.
    """
    queryset = LacRegion.objects.all()
    serializer_class = LacRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LaveriesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LaveriesFontPoint.
    """
    queryset = LaveriesFontPoint.objects.all()
    serializer_class = LaveriesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'quartier', 'standing']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Layer.
    """
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['schema_name', 'table_name', 'feature_column']

class LeMfoundiPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LeMfoundiPolyline.
    """
    queryset = LeMfoundiPolyline.objects.all()
    serializer_class = LeMfoundiPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['nom', 'sens']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LieuxRemarquablesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LieuxRemarquablesCustomPoint.
    """
    queryset = LieuxRemarquablesCustomPoint.objects.all()
    serializer_class = LieuxRemarquablesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['descriptio', 'nom']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LieuxRemarquablesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LieuxRemarquablesFontPoint.
    """
    queryset = LieuxRemarquablesFontPoint.objects.all()
    serializer_class = LieuxRemarquablesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['descriptio', 'nom']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LieuxRemarquablesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LieuxRemarquablesPoint.
    """
    queryset = LieuxRemarquablesPoint.objects.all()
    serializer_class = LieuxRemarquablesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['descriptio', 'nom']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LigneBusPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LigneBusPolyline.
    """
    queryset = LigneBusPolyline.objects.all()
    serializer_class = LigneBusPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['lineaire', 'designatio']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LigneBusProjetPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LigneBusProjetPolyline.
    """
    queryset = LigneBusProjetPolyline.objects.all()
    serializer_class = LigneBusProjetPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['num_ligne', 'itineraire']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LimiteMokoloPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LimiteMokoloPolyline.
    """
    queryset = LimiteMokoloPolyline.objects.all()
    serializer_class = LimiteMokoloPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['sup']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LimiteYdeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LimiteYde.
    """
    queryset = LimiteYde.objects.all()
    serializer_class = LimiteYdeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['minatd', 'code_prov', 'departemen', 'départemen', 'province', 'chef_lieu']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LimiteYde1RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LimiteYde1Region.
    """
    queryset = LimiteYde1Region.objects.all()
    serializer_class = LimiteYde1RegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['commune']
    search_fields = ['commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class LimitesDesCommunesYdeRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for LimitesDesCommunesYdeRegion.
    """
    queryset = LimitesDesCommunesYdeRegion.objects.all()
    serializer_class = LimitesDesCommunesYdeRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['commune']
    search_fields = ['commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MairiesYaoundeCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MairiesYaoundeCustomPoint.
    """
    queryset = MairiesYaoundeCustomPoint.objects.all()
    serializer_class = MairiesYaoundeCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarcheEligedzoaRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarcheEligedzoaRegion.
    """
    queryset = MarcheEligedzoaRegion.objects.all()
    serializer_class = MarcheEligedzoaRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['nommarche', 'nbreboutiq', 'nbrehangar', 'pricipalea']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarcheEligedzoaZoneActiviteRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarcheEligedzoaZoneActiviteRegion.
    """
    queryset = MarcheEligedzoaZoneActiviteRegion.objects.all()
    serializer_class = MarcheEligedzoaZoneActiviteRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['nommarche', 'nbreboutiq', 'nbrehangar', 'pricipalea']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarcheMokoloRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarcheMokoloRegion.
    """
    queryset = MarcheMokoloRegion.objects.all()
    serializer_class = MarcheMokoloRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarchesCommunauxCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarchesCommunauxCuyPoint.
    """
    queryset = MarchesCommunauxCuyPoint.objects.all()
    serializer_class = MarchesCommunauxCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarchesCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarchesCuyPoint.
    """
    queryset = MarchesCuyPoint.objects.all()
    serializer_class = MarchesCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['commune', 'quartier']
    search_fields = ['designatio', 'commune', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarchesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarchesPoint.
    """
    queryset = MarchesPoint.objects.all()
    serializer_class = MarchesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MarchesRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MarchesRegion.
    """
    queryset = MarchesRegion.objects.all()
    serializer_class = MarchesRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MinisteresYaoundeCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MinisteresYaoundeCustomPoint.
    """
    queryset = MinisteresYaoundeCustomPoint.objects.all()
    serializer_class = MinisteresYaoundeCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'sigle', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MonumentsEllipseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MonumentsEllipse.
    """
    queryset = MonumentsEllipse.objects.all()
    serializer_class = MonumentsEllipseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['monument', 'position', 'creation', 'significat']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MonumentsRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MonumentsRegion.
    """
    queryset = MonumentsRegion.objects.all()
    serializer_class = MonumentsRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['monument', 'position', 'creation', 'significat']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MosqueesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MosqueesFontPoint.
    """
    queryset = MosqueesFontPoint.objects.all()
    serializer_class = MosqueesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class MursPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MursPolyline.
    """
    queryset = MursPolyline.objects.all()
    serializer_class = MursPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class NationsUniesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for NationsUniesPoint.
    """
    queryset = NationsUniesPoint.objects.all()
    serializer_class = NationsUniesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ParkingsCuy2007PolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ParkingsCuy2007Polyline.
    """
    queryset = ParkingsCuy2007Polyline.objects.all()
    serializer_class = ParkingsCuy2007PolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['libelle', 'pr_pt', 'localisati', 'observatio']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ParkingsCuyPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ParkingsCuyPolyline.
    """
    queryset = ParkingsCuyPolyline.objects.all()
    serializer_class = ParkingsCuyPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['localisati', 'num_rue', 'nature']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class PharmaciesPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for PharmaciesPoint.
    """
    queryset = PharmaciesPoint.objects.all()
    serializer_class = PharmaciesPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'arrondisse']
    search_fields = ['noms', 'localisati', 'pharmacien', 't_l_phone', 'bo_te_post', 'quartier', 'arrondisse', 'ouverture']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class PrefecturesSousPrefecturesCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for PrefecturesSousPrefecturesCustomPoint.
    """
    queryset = PrefecturesSousPrefecturesCustomPoint.objects.all()
    serializer_class = PrefecturesSousPrefecturesCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['numero', 'nom', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ProjetsRouteEllipseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ProjetsRouteEllipse.
    """
    queryset = ProjetsRouteEllipse.objects.all()
    serializer_class = ProjetsRouteEllipseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['lineaire']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ProjetsRoutePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ProjetsRoutePolyline.
    """
    queryset = ProjetsRoutePolyline.objects.all()
    serializer_class = ProjetsRoutePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['lineaire']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class QuadrillageNoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint for QuadrillageNone.
    """
    queryset = QuadrillageNone.objects.all()
    serializer_class = QuadrillageNoneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['recule', 'alignement', 'obli_archi', 'cloture', 'interdits', 'voirie']

class QuadrillagePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for QuadrillagePoint.
    """
    queryset = QuadrillagePoint.objects.all()
    serializer_class = QuadrillagePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['recule', 'alignement', 'obli_archi', 'cloture', 'interdits', 'voirie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class QuadrillageRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for QuadrillageRegion.
    """
    queryset = QuadrillageRegion.objects.all()
    serializer_class = QuadrillageRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['recule', 'alignement', 'obli_archi', 'cloture', 'interdits', 'voirie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class QuartierRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for QuartierRegion.
    """
    queryset = QuartierRegion.objects.all()
    serializer_class = QuartierRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'arrondisse']
    search_fields = ['quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class QuartiersPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for QuartiersPoint.
    """
    queryset = QuartiersPoint.objects.all()
    serializer_class = QuartiersPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['texte', 'equipement']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RadioYaoundeCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RadioYaoundeCustomPoint.
    """
    queryset = RadioYaoundeCustomPoint.objects.all()
    serializer_class = RadioYaoundeCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'frequence', 'typologie', 'localisati', 'quartier', 'arrondisse', 'statut']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ReligionsYaoundeFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ReligionsYaoundeFontPoint.
    """
    queryset = ReligionsYaoundeFontPoint.objects.all()
    serializer_class = ReligionsYaoundeFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'postale', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ReligionsYaoundePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ReligionsYaoundePoint.
    """
    queryset = ReligionsYaoundePoint.objects.all()
    serializer_class = ReligionsYaoundePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier']
    search_fields = ['nom', 'telephone', 'postale', 'quartier', 'religion', 'categorie']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ReseauEpPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ReseauEpPolyline.
    """
    queryset = ReseauEpPolyline.objects.all()
    serializer_class = ReseauEpPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['ep']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RestaurantsYaoundeFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RestaurantsYaoundeFontPoint.
    """
    queryset = RestaurantsYaoundeFontPoint.objects.all()
    serializer_class = RestaurantsYaoundeFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'commune']
    search_fields = ['nom', 't_lephone', 'quartier', 'standing', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RivieresPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RivieresPolyline.
    """
    queryset = RivieresPolyline.objects.all()
    serializer_class = RivieresPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['nom', 'sens']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RivieresRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RivieresRegion.
    """
    queryset = RivieresRegion.objects.all()
    serializer_class = RivieresRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom']
    search_fields = ['nom', 'sens']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RouteEnProjetPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RouteEnProjetPolyline.
    """
    queryset = RouteEnProjetPolyline.objects.all()
    serializer_class = RouteEnProjetPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['numero', 'nom_rue']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class SanitaireYaoundePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for SanitaireYaoundePoint.
    """
    queryset = SanitaireYaoundePoint.objects.all()
    serializer_class = SanitaireYaoundePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'commune', 'quartier']
    search_fields = ['nom', 'statut', 'categorie', 'promoteur', 't_lephone', 'postale', 'de_sante0', 'district', 'commune', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class SapeursPompierPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for SapeursPompierPoint.
    """
    queryset = SapeursPompierPoint.objects.all()
    serializer_class = SapeursPompierPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ServicesCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ServicesCuyPoint.
    """
    queryset = ServicesCuyPoint.objects.all()
    serializer_class = ServicesCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class StationsSevicesFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for StationsSevicesFontPoint.
    """
    queryset = StationsSevicesFontPoint.objects.all()
    serializer_class = StationsSevicesFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['nom', 'quartier', 'arrondisse']
    search_fields = ['nom', 'quartier', 'arrondisse']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class SupZoneUrbaRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for SupZoneUrbaRegion.
    """
    queryset = SupZoneUrbaRegion.objects.all()
    serializer_class = SupZoneUrbaRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class TerrainsDeSportsCustomPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for TerrainsDeSportsCustomPoint.
    """
    queryset = TerrainsDeSportsCustomPoint.objects.all()
    serializer_class = TerrainsDeSportsCustomPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier', 'commune']
    search_fields = ['noms', 'type', 'standing', 'quartier', 'discipline', 'commune']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ToilettesPubliquesCuyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ToilettesPubliquesCuyPoint.
    """
    queryset = ToilettesPubliquesCuyPoint.objects.all()
    serializer_class = ToilettesPubliquesCuyPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['quartier']
    search_fields = ['designatio', 'observatri', 'quartier']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class TopologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Topology.
    """
    queryset = Topology.objects.all()
    serializer_class = TopologySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class VoieFerreePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for VoieFerreePolyline.
    """
    queryset = VoieFerreePolyline.objects.all()
    serializer_class = VoieFerreePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class VoiriesYaoundePointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for VoiriesYaoundePoint.
    """
    queryset = VoiriesYaoundePoint.objects.all()
    serializer_class = VoiriesYaoundePointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class VoiriesYaoundePolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for VoiriesYaoundePolyline.
    """
    queryset = VoiriesYaoundePolyline.objects.all()
    serializer_class = VoiriesYaoundePolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = []
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class WorldFontPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for WorldFontPoint.
    """
    queryset = WorldFontPoint.objects.all()
    serializer_class = WorldFontPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['country']
    search_fields = ['country', 'capital', 'continent', 'fips', 'iso_2', 'iso_3']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class WorldPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for WorldPolyline.
    """
    queryset = WorldPolyline.objects.all()
    serializer_class = WorldPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['country']
    search_fields = ['country', 'capital', 'continent', 'fips', 'iso_2', 'iso_3']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class WorldRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for WorldRegion.
    """
    queryset = WorldRegion.objects.all()
    serializer_class = WorldRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = ['country']
    search_fields = ['country', 'capital', 'continent', 'fips', 'iso_2', 'iso_3']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C121CPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C121CPolyline.
    """
    queryset = Z1C121CPolyline.objects.all()
    serializer_class = Z1C121CPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone1', 'number_2_1_c']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C122CPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C122CPoint.
    """
    queryset = Z1C122CPoint.objects.all()
    serializer_class = Z1C122CPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C122CPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C122CPolyline.
    """
    queryset = Z1C122CPolyline.objects.all()
    serializer_class = Z1C122CPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C131CPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C131CPolyline.
    """
    queryset = Z1C131CPolyline.objects.all()
    serializer_class = Z1C131CPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C132CPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C132CPolyline.
    """
    queryset = Z1C132CPolyline.objects.all()
    serializer_class = Z1C132CPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class Z1C133CPolylineViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Z1C133CPolyline.
    """
    queryset = Z1C133CPolyline.objects.all()
    serializer_class = Z1C133CPolylineSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'circuit']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ZoneAdressageRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ZoneAdressageRegion.
    """
    queryset = ZoneAdressageRegion.objects.all()
    serializer_class = ZoneAdressageRegionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['nom_zone']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ZonesProscritesEllipseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ZonesProscritesEllipse.
    """
    queryset = ZonesProscritesEllipse.objects.all()
    serializer_class = ZonesProscritesEllipseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, InBBoxFilter, DistanceToPointFilter]
    filterset_fields = []
    search_fields = ['zone', 'itineraire']
    bbox_filter_field = 'geom'
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

