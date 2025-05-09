from rest_framework import routers
from .api_views import (
    AfricaRegionViewSet,
    AgencesDeVoyagesFontPointViewSet,
    AmbassadesPointViewSet,
    ArmeeFontPointViewSet,
    ArrondAireMetropViewSet,
    AubergesCustomPointViewSet,
    AxesVoiriesPolylineViewSet,
    BacsFontPointViewSet,
    BacsPointViewSet,
    BanquesEtMicrofinancesCustomPointViewSet,
    BassinVersantMfoundiBasRegionViewSet,
    BassinVersantMfoundiRegionViewSet,
    BassinVersantNoneViewSet,
    BassinVersantRegionViewSet,
    BatiDurPolylineViewSet,
    BatiLocauxPolylineViewSet,
    BatiPublicsPointViewSet,
    BatiPublicsRegionViewSet,
    BatimentsYaoundePointViewSet,
    BatimentsYaoundePolylineViewSet,
    BatimentsYaoundeRegionViewSet,
    BouchesIncendiesYdeCustomPointViewSet,
    BouchesIncendiesYdePointViewSet,
    BoulangeriesCustomPointViewSet,
    BoulangeriesRegionViewSet,
    CampSicCustomPointViewSet,
    CentreSpecialDetatCivilFontPointViewSet,
    CentresCulturelsCustomPointViewSet,
    CimetiereRegionViewSet,
    CinemaCustomPointViewSet,
    CitesMunicipalesCuyPointViewSet,
    CommissariatsYdeFontPointViewSet,
    ComplexesSportifsCustomPointViewSet,
    ConsulatsPointViewSet,
    DelegationsCustomPointViewSet,
    DepAireMetropViewSet,
    EcoleNormaleDesInstituteursDenseignementGeneralPointViewSet,
    EcolesMatPrimairePointViewSet,
    EglisesCatholiquesFontPointViewSet,
    EglisesPresbyteriennesFontPointViewSet,
    EglisesProtestantesPointViewSet,
    EnseignementDeBaseFontPointViewSet,
    EnseignementMaternelleCustomPointViewSet,
    EnseignementMaternelleRegionViewSet,
    EnseignementPrimaireFontPointViewSet,
    EnseignementPrimaireRegionViewSet,
    EnseignementSuperieurCustomPointViewSet,
    EnseignementsSecondairesFinalPointViewSet,
    EspaceVertEllipseViewSet,
    EspaceVertRegionViewSet,
    EspacesAmenagesRegionViewSet,
    EtalonnagePolylineViewSet,
    FeuTricoloreCustomPointViewSet,
    FeuTricoloreEllipseViewSet,
    FeuTricolorePolylineViewSet,
    FeuTricoloreRegionViewSet,
    GaragesCustomPointViewSet,
    GareFerroviaireCustomPointViewSet,
    GaresRoutieresCuyPointViewSet,
    GendarmeriesPointViewSet,
    HangarsPolylineViewSet,
    HotelsFontPointViewSet,
    HussiersYdeCustomPointViewSet,
    ItinerairePrcPolylineViewSet,
    LacHorsCartoRegionViewSet,
    LacRegionViewSet,
    LaveriesFontPointViewSet,
    LayerViewSet,
    LeMfoundiPolylineViewSet,
    LieuxRemarquablesCustomPointViewSet,
    LieuxRemarquablesFontPointViewSet,
    LieuxRemarquablesPointViewSet,
    LigneBusPolylineViewSet,
    LigneBusProjetPolylineViewSet,
    LimiteMokoloPolylineViewSet,
    LimiteYdeViewSet,
    LimiteYde1RegionViewSet,
    LimitesDesCommunesYdeRegionViewSet,
    MairiesYaoundeCustomPointViewSet,
    MarcheEligedzoaRegionViewSet,
    MarcheEligedzoaZoneActiviteRegionViewSet,
    MarcheMokoloRegionViewSet,
    MarchesCommunauxCuyPointViewSet,
    MarchesCuyPointViewSet,
    MarchesPointViewSet,
    MarchesRegionViewSet,
    MinisteresYaoundeCustomPointViewSet,
    MonumentsEllipseViewSet,
    MonumentsRegionViewSet,
    MosqueesFontPointViewSet,
    MursPolylineViewSet,
    NationsUniesPointViewSet,
    ParkingsCuy2007PolylineViewSet,
    ParkingsCuyPolylineViewSet,
    PharmaciesPointViewSet,
    PrefecturesSousPrefecturesCustomPointViewSet,
    ProjetsRouteEllipseViewSet,
    ProjetsRoutePolylineViewSet,
    QuadrillageNoneViewSet,
    QuadrillagePointViewSet,
    QuadrillageRegionViewSet,
    QuartierRegionViewSet,
    QuartiersPointViewSet,
    RadioYaoundeCustomPointViewSet,
    ReligionsYaoundeFontPointViewSet,
    ReligionsYaoundePointViewSet,
    ReseauEpPolylineViewSet,
    RestaurantsYaoundeFontPointViewSet,
    RivieresPolylineViewSet,
    RivieresRegionViewSet,
    RouteEnProjetPolylineViewSet,
    SanitaireYaoundePointViewSet,
    SapeursPompierPointViewSet,
    ServicesCuyPointViewSet,
    StationsSevicesFontPointViewSet,
    SupZoneUrbaRegionViewSet,
    TerrainsDeSportsCustomPointViewSet,
    ToilettesPubliquesCuyPointViewSet,
    TopologyViewSet,
    VoieFerreePolylineViewSet,
    VoiriesYaoundePointViewSet,
    VoiriesYaoundePolylineViewSet,
    WorldFontPointViewSet,
    WorldPolylineViewSet,
    WorldRegionViewSet,
    Z1C121CPolylineViewSet,
    Z1C122CPointViewSet,
    Z1C122CPolylineViewSet,
    Z1C131CPolylineViewSet,
    Z1C132CPolylineViewSet,
    Z1C133CPolylineViewSet,
    ZoneAdressageRegionViewSet,
    ZonesProscritesEllipseViewSet
)

app_name = "buildings"
router = routers.DefaultRouter()
router.register(r'africa', AfricaRegionViewSet)
router.register(r'agences-de-voyages-font', AgencesDeVoyagesFontPointViewSet)
router.register(r'ambassades', AmbassadesPointViewSet)
router.register(r'armee-font', ArmeeFontPointViewSet)
router.register(r'arrond-aire-metrop', ArrondAireMetropViewSet)
router.register(r'auberges-custom', AubergesCustomPointViewSet)
router.register(r'axes-voiries', AxesVoiriesPolylineViewSet)
router.register(r'bacs-font', BacsFontPointViewSet)
router.register(r'bacs', BacsPointViewSet)
router.register(r'banques-et-microfinances-custom', BanquesEtMicrofinancesCustomPointViewSet)
router.register(r'bassin-versant-mfoundi-bas', BassinVersantMfoundiBasRegionViewSet)
router.register(r'bassin-versant-mfoundi', BassinVersantMfoundiRegionViewSet)
router.register(r'bassin-versant-none', BassinVersantNoneViewSet)
router.register(r'bassin-versant', BassinVersantRegionViewSet)
router.register(r'bati-dur', BatiDurPolylineViewSet)
router.register(r'bati-locaux', BatiLocauxPolylineViewSet)
router.register(r'bati-publics', BatiPublicsPointViewSet)
router.register(r'bati-publics', BatiPublicsRegionViewSet)
router.register(r'batiments-yaounde', BatimentsYaoundePointViewSet)
router.register(r'batiments-yaounde', BatimentsYaoundePolylineViewSet)
router.register(r'batiments-yaounde', BatimentsYaoundeRegionViewSet)
router.register(r'bouches-incendies-yde-custom', BouchesIncendiesYdeCustomPointViewSet)
router.register(r'bouches-incendies-yde', BouchesIncendiesYdePointViewSet)
router.register(r'boulangeries-custom', BoulangeriesCustomPointViewSet)
router.register(r'boulangeries', BoulangeriesRegionViewSet)
router.register(r'camp-sic-custom', CampSicCustomPointViewSet)
router.register(r'centre-special-detat-civil-font', CentreSpecialDetatCivilFontPointViewSet)
router.register(r'centres-culturels-custom', CentresCulturelsCustomPointViewSet)
router.register(r'cimetiere', CimetiereRegionViewSet)
router.register(r'cinema-custom', CinemaCustomPointViewSet)
router.register(r'cites-municipales-cuy', CitesMunicipalesCuyPointViewSet)
router.register(r'commissariats-yde-font', CommissariatsYdeFontPointViewSet)
router.register(r'complexes-sportifs-custom', ComplexesSportifsCustomPointViewSet)
router.register(r'consulats', ConsulatsPointViewSet)
router.register(r'delegations-custom', DelegationsCustomPointViewSet)
router.register(r'dep-aire-metrop', DepAireMetropViewSet)
router.register(r'ecole-normale-des-instituteurs-denseignement-general', EcoleNormaleDesInstituteursDenseignementGeneralPointViewSet)
router.register(r'ecoles-mat-primaire', EcolesMatPrimairePointViewSet)
router.register(r'eglises-catholiques-font', EglisesCatholiquesFontPointViewSet)
router.register(r'eglises-presbyteriennes-font', EglisesPresbyteriennesFontPointViewSet)
router.register(r'eglises-protestantes', EglisesProtestantesPointViewSet)
router.register(r'enseignement-de-base-font', EnseignementDeBaseFontPointViewSet)
router.register(r'enseignement-maternelle-custom', EnseignementMaternelleCustomPointViewSet)
router.register(r'enseignement-maternelle', EnseignementMaternelleRegionViewSet)
router.register(r'enseignement-primaire-font', EnseignementPrimaireFontPointViewSet)
router.register(r'enseignement-primaire', EnseignementPrimaireRegionViewSet)
router.register(r'enseignement-superieur-custom', EnseignementSuperieurCustomPointViewSet)
router.register(r'enseignements-secondaires-final', EnseignementsSecondairesFinalPointViewSet)
router.register(r'espace-vert-ellipse', EspaceVertEllipseViewSet)
router.register(r'espace-vert', EspaceVertRegionViewSet)
router.register(r'espaces-amenages', EspacesAmenagesRegionViewSet)
router.register(r'etalonnage', EtalonnagePolylineViewSet)
router.register(r'feu-tricolore-custom', FeuTricoloreCustomPointViewSet)
router.register(r'feu-tricolore-ellipse', FeuTricoloreEllipseViewSet)
router.register(r'feu-tricolore', FeuTricolorePolylineViewSet)
router.register(r'feu-tricolore', FeuTricoloreRegionViewSet)
router.register(r'garages-custom', GaragesCustomPointViewSet)
router.register(r'gare-ferroviaire-custom', GareFerroviaireCustomPointViewSet)
router.register(r'gares-routieres-cuy', GaresRoutieresCuyPointViewSet)
router.register(r'gendarmeries', GendarmeriesPointViewSet)
router.register(r'hangars', HangarsPolylineViewSet)
router.register(r'hotels-font', HotelsFontPointViewSet)
router.register(r'hussiers-yde-custom', HussiersYdeCustomPointViewSet)
router.register(r'itineraire-prc', ItinerairePrcPolylineViewSet)
router.register(r'lac-hors-carto', LacHorsCartoRegionViewSet)
router.register(r'lac', LacRegionViewSet)
router.register(r'laveries-font', LaveriesFontPointViewSet)
router.register(r'layer', LayerViewSet)
router.register(r'le-mfoundi', LeMfoundiPolylineViewSet)
router.register(r'lieux-remarquables-custom', LieuxRemarquablesCustomPointViewSet)
router.register(r'lieux-remarquables-font', LieuxRemarquablesFontPointViewSet)
router.register(r'lieux-remarquables', LieuxRemarquablesPointViewSet)
router.register(r'ligne-bus', LigneBusPolylineViewSet)
router.register(r'ligne-bus-projet', LigneBusProjetPolylineViewSet)
router.register(r'limite-mokolo', LimiteMokoloPolylineViewSet)
router.register(r'limite-yde', LimiteYdeViewSet)
router.register(r'limite-yde1', LimiteYde1RegionViewSet)
router.register(r'limites-des-communes-yde', LimitesDesCommunesYdeRegionViewSet)
router.register(r'mairies-yaounde-custom', MairiesYaoundeCustomPointViewSet)
router.register(r'marche-eligedzoa', MarcheEligedzoaRegionViewSet)
router.register(r'marche-eligedzoa-zone-activite', MarcheEligedzoaZoneActiviteRegionViewSet)
router.register(r'marche-mokolo', MarcheMokoloRegionViewSet)
router.register(r'marches-communaux-cuy', MarchesCommunauxCuyPointViewSet)
router.register(r'marches-cuy', MarchesCuyPointViewSet)
router.register(r'marches', MarchesPointViewSet)
router.register(r'marches', MarchesRegionViewSet)
router.register(r'ministeres-yaounde-custom', MinisteresYaoundeCustomPointViewSet)
router.register(r'monuments-ellipse', MonumentsEllipseViewSet)
router.register(r'monuments', MonumentsRegionViewSet)
router.register(r'mosquees-font', MosqueesFontPointViewSet)
router.register(r'murs', MursPolylineViewSet)
router.register(r'nations-unies', NationsUniesPointViewSet)
router.register(r'parkings-cuy2007', ParkingsCuy2007PolylineViewSet)
router.register(r'parkings-cuy', ParkingsCuyPolylineViewSet)
router.register(r'pharmacies', PharmaciesPointViewSet)
router.register(r'prefectures-sous-prefectures-custom', PrefecturesSousPrefecturesCustomPointViewSet)
router.register(r'projets-route-ellipse', ProjetsRouteEllipseViewSet)
router.register(r'projets-route', ProjetsRoutePolylineViewSet)
router.register(r'quadrillage-none', QuadrillageNoneViewSet)
router.register(r'quadrillage', QuadrillagePointViewSet)
router.register(r'quadrillage', QuadrillageRegionViewSet)
router.register(r'quartier', QuartierRegionViewSet)
router.register(r'quartiers', QuartiersPointViewSet)
router.register(r'radio-yaounde-custom', RadioYaoundeCustomPointViewSet)
router.register(r'religions-yaounde-font', ReligionsYaoundeFontPointViewSet)
router.register(r'religions-yaounde', ReligionsYaoundePointViewSet)
router.register(r'reseau-ep', ReseauEpPolylineViewSet)
router.register(r'restaurants-yaounde-font', RestaurantsYaoundeFontPointViewSet)
router.register(r'rivieres', RivieresPolylineViewSet)
router.register(r'rivieres', RivieresRegionViewSet)
router.register(r'route-en-projet', RouteEnProjetPolylineViewSet)
router.register(r'sanitaire-yaounde', SanitaireYaoundePointViewSet)
router.register(r'sapeurs-pompier', SapeursPompierPointViewSet)
router.register(r'services-cuy', ServicesCuyPointViewSet)
router.register(r'stations-sevices-font', StationsSevicesFontPointViewSet)
router.register(r'sup-zone-urba', SupZoneUrbaRegionViewSet)
router.register(r'terrains-de-sports-custom', TerrainsDeSportsCustomPointViewSet)
router.register(r'toilettes-publiques-cuy', ToilettesPubliquesCuyPointViewSet)
router.register(r'topology', TopologyViewSet)
router.register(r'voie-ferree', VoieFerreePolylineViewSet)
router.register(r'voiries-yaounde', VoiriesYaoundePointViewSet)
router.register(r'voiries-yaounde', VoiriesYaoundePolylineViewSet)
router.register(r'world-font', WorldFontPointViewSet)
router.register(r'world', WorldPolylineViewSet)
router.register(r'world', WorldRegionViewSet)
router.register(r'z1-c121-cpolyline', Z1C121CPolylineViewSet)
router.register(r'z1-c122-cpoint', Z1C122CPointViewSet)
router.register(r'z1-c122-cpolyline', Z1C122CPolylineViewSet)
router.register(r'z1-c131-cpolyline', Z1C131CPolylineViewSet)
router.register(r'z1-c132-cpolyline', Z1C132CPolylineViewSet)
router.register(r'z1-c133-cpolyline', Z1C133CPolylineViewSet)
router.register(r'zone-adressage', ZoneAdressageRegionViewSet)
router.register(r'zones-proscrites-ellipse', ZonesProscritesEllipseViewSet)


urlpatterns = router.urls
