from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
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

class AfricaRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AfricaRegion
        geo_field = 'geom'
        fields = '__all__'

class AgencesDeVoyagesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AgencesDeVoyagesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class AmbassadesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AmbassadesPoint
        geo_field = 'geom'
        fields = '__all__'

class ArmeeFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ArmeeFontPoint
        geo_field = 'geom'
        fields = '__all__'

class ArrondAireMetropSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ArrondAireMetrop
        geo_field = 'geom'
        fields = '__all__'

class AubergesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AubergesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class AxesVoiriesPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AxesVoiriesPolyline
        geo_field = 'geom'
        fields = '__all__'

class BacsFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BacsFontPoint
        geo_field = 'geom'
        fields = '__all__'

class BacsPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BacsPoint
        geo_field = 'geom'
        fields = '__all__'

class BanquesEtMicrofinancesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BanquesEtMicrofinancesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class BassinVersantMfoundiBasRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BassinVersantMfoundiBasRegion
        geo_field = 'geom'
        fields = '__all__'

class BassinVersantMfoundiRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BassinVersantMfoundiRegion
        geo_field = 'geom'
        fields = '__all__'

class BassinVersantNoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BassinVersantNone
        fields = '__all__'

class BassinVersantRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BassinVersantRegion
        geo_field = 'geom'
        fields = '__all__'

class BatiDurPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatiDurPolyline
        geo_field = 'geom'
        fields = '__all__'

class BatiLocauxPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatiLocauxPolyline
        geo_field = 'geom'
        fields = '__all__'

class BatiPublicsPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatiPublicsPoint
        geo_field = 'geom'
        fields = '__all__'

class BatiPublicsRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatiPublicsRegion
        geo_field = 'geom'
        fields = '__all__'

class BatimentsYaoundePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatimentsYaoundePoint
        geo_field = 'geom'
        fields = '__all__'

class BatimentsYaoundePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatimentsYaoundePolyline
        geo_field = 'geom'
        fields = '__all__'

class BatimentsYaoundeRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BatimentsYaoundeRegion
        geo_field = 'geom'
        fields = '__all__'

class BouchesIncendiesYdeCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BouchesIncendiesYdeCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class BouchesIncendiesYdePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BouchesIncendiesYdePoint
        geo_field = 'geom'
        fields = '__all__'

class BoulangeriesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BoulangeriesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class BoulangeriesRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BoulangeriesRegion
        geo_field = 'geom'
        fields = '__all__'

class CampSicCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CampSicCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class CentreSpecialDetatCivilFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CentreSpecialDetatCivilFontPoint
        geo_field = 'geom'
        fields = '__all__'

class CentresCulturelsCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CentresCulturelsCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class CimetiereRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CimetiereRegion
        geo_field = 'geom'
        fields = '__all__'

class CinemaCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CinemaCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class CitesMunicipalesCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CitesMunicipalesCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class CommissariatsYdeFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CommissariatsYdeFontPoint
        geo_field = 'geom'
        fields = '__all__'

class ComplexesSportifsCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ComplexesSportifsCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class ConsulatsPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConsulatsPoint
        geo_field = 'geom'
        fields = '__all__'

class DelegationsCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DelegationsCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class DepAireMetropSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DepAireMetrop
        geo_field = 'geom'
        fields = '__all__'

class EcoleNormaleDesInstituteursDenseignementGeneralPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EcoleNormaleDesInstituteursDenseignementGeneralPoint
        geo_field = 'geom'
        fields = '__all__'

class EcolesMatPrimairePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EcolesMatPrimairePoint
        geo_field = 'geom'
        fields = '__all__'

class EglisesCatholiquesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EglisesCatholiquesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class EglisesPresbyteriennesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EglisesPresbyteriennesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class EglisesProtestantesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EglisesProtestantesPoint
        geo_field = 'geom'
        fields = '__all__'

class EnseignementDeBaseFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementDeBaseFontPoint
        geo_field = 'geom'
        fields = '__all__'

class EnseignementMaternelleCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementMaternelleCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class EnseignementMaternelleRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementMaternelleRegion
        geo_field = 'geom'
        fields = '__all__'

class EnseignementPrimaireFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementPrimaireFontPoint
        geo_field = 'geom'
        fields = '__all__'

class EnseignementPrimaireRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementPrimaireRegion
        geo_field = 'geom'
        fields = '__all__'

class EnseignementSuperieurCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementSuperieurCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class EnseignementsSecondairesFinalPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EnseignementsSecondairesFinalPoint
        geo_field = 'geom'
        fields = '__all__'

class EspaceVertEllipseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EspaceVertEllipse
        geo_field = 'geom'
        fields = '__all__'

class EspaceVertRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EspaceVertRegion
        geo_field = 'geom'
        fields = '__all__'

class EspacesAmenagesRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EspacesAmenagesRegion
        geo_field = 'geom'
        fields = '__all__'

class EtalonnagePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EtalonnagePolyline
        geo_field = 'geom'
        fields = '__all__'

class FeuTricoloreCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = FeuTricoloreCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class FeuTricoloreEllipseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = FeuTricoloreEllipse
        geo_field = 'geom'
        fields = '__all__'

class FeuTricolorePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = FeuTricolorePolyline
        geo_field = 'geom'
        fields = '__all__'

class FeuTricoloreRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = FeuTricoloreRegion
        geo_field = 'geom'
        fields = '__all__'

class GaragesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GaragesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class GareFerroviaireCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GareFerroviaireCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class GaresRoutieresCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GaresRoutieresCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class GendarmeriesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GendarmeriesPoint
        geo_field = 'geom'
        fields = '__all__'

class HangarsPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HangarsPolyline
        geo_field = 'geom'
        fields = '__all__'

class HotelsFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HotelsFontPoint
        geo_field = 'geom'
        fields = '__all__'

class HussiersYdeCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HussiersYdeCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class ItinerairePrcPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ItinerairePrcPolyline
        geo_field = 'geom'
        fields = '__all__'

class LacHorsCartoRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LacHorsCartoRegion
        geo_field = 'geom'
        fields = '__all__'

class LacRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LacRegion
        geo_field = 'geom'
        fields = '__all__'

class LaveriesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LaveriesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'

class LeMfoundiPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LeMfoundiPolyline
        geo_field = 'geom'
        fields = '__all__'

class LieuxRemarquablesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LieuxRemarquablesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class LieuxRemarquablesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LieuxRemarquablesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class LieuxRemarquablesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LieuxRemarquablesPoint
        geo_field = 'geom'
        fields = '__all__'

class LigneBusPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LigneBusPolyline
        geo_field = 'geom'
        fields = '__all__'

class LigneBusProjetPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LigneBusProjetPolyline
        geo_field = 'geom'
        fields = '__all__'

class LimiteMokoloPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LimiteMokoloPolyline
        geo_field = 'geom'
        fields = '__all__'

class LimiteYdeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LimiteYde
        geo_field = 'geom'
        fields = '__all__'

class LimiteYde1RegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LimiteYde1Region
        geo_field = 'geom'
        fields = '__all__'

class LimitesDesCommunesYdeRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LimitesDesCommunesYdeRegion
        geo_field = 'geom'
        fields = '__all__'

class MairiesYaoundeCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MairiesYaoundeCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class MarcheEligedzoaRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarcheEligedzoaRegion
        geo_field = 'geom'
        fields = '__all__'

class MarcheEligedzoaZoneActiviteRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarcheEligedzoaZoneActiviteRegion
        geo_field = 'geom'
        fields = '__all__'

class MarcheMokoloRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarcheMokoloRegion
        geo_field = 'geom'
        fields = '__all__'

class MarchesCommunauxCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarchesCommunauxCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class MarchesCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarchesCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class MarchesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarchesPoint
        geo_field = 'geom'
        fields = '__all__'

class MarchesRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarchesRegion
        geo_field = 'geom'
        fields = '__all__'

class MinisteresYaoundeCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MinisteresYaoundeCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class MonumentsEllipseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MonumentsEllipse
        geo_field = 'geom'
        fields = '__all__'

class MonumentsRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MonumentsRegion
        geo_field = 'geom'
        fields = '__all__'

class MosqueesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MosqueesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class MursPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MursPolyline
        geo_field = 'geom'
        fields = '__all__'

class NationsUniesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = NationsUniesPoint
        geo_field = 'geom'
        fields = '__all__'

class ParkingsCuy2007PolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ParkingsCuy2007Polyline
        geo_field = 'geom'
        fields = '__all__'

class ParkingsCuyPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ParkingsCuyPolyline
        geo_field = 'geom'
        fields = '__all__'

class PharmaciesPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PharmaciesPoint
        geo_field = 'geom'
        fields = '__all__'

class PrefecturesSousPrefecturesCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PrefecturesSousPrefecturesCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class ProjetsRouteEllipseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ProjetsRouteEllipse
        geo_field = 'geom'
        fields = '__all__'

class ProjetsRoutePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ProjetsRoutePolyline
        geo_field = 'geom'
        fields = '__all__'

class QuadrillageNoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuadrillageNone
        fields = '__all__'

class QuadrillagePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuadrillagePoint
        geo_field = 'geom'
        fields = '__all__'

class QuadrillageRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuadrillageRegion
        geo_field = 'geom'
        fields = '__all__'

class QuartierRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuartierRegion
        geo_field = 'geom'
        fields = '__all__'

class QuartiersPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuartiersPoint
        geo_field = 'geom'
        fields = '__all__'

class RadioYaoundeCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RadioYaoundeCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class ReligionsYaoundeFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ReligionsYaoundeFontPoint
        geo_field = 'geom'
        fields = '__all__'

class ReligionsYaoundePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ReligionsYaoundePoint
        geo_field = 'geom'
        fields = '__all__'

class ReseauEpPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ReseauEpPolyline
        geo_field = 'geom'
        fields = '__all__'

class RestaurantsYaoundeFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RestaurantsYaoundeFontPoint
        geo_field = 'geom'
        fields = '__all__'

class RivieresPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RivieresPolyline
        geo_field = 'geom'
        fields = '__all__'

class RivieresRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RivieresRegion
        geo_field = 'geom'
        fields = '__all__'

class RouteEnProjetPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RouteEnProjetPolyline
        geo_field = 'geom'
        fields = '__all__'

class SanitaireYaoundePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SanitaireYaoundePoint
        geo_field = 'geom'
        fields = '__all__'

class SapeursPompierPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SapeursPompierPoint
        geo_field = 'geom'
        fields = '__all__'

class ServicesCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServicesCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class StationsSevicesFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = StationsSevicesFontPoint
        geo_field = 'geom'
        fields = '__all__'

class SupZoneUrbaRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SupZoneUrbaRegion
        geo_field = 'geom'
        fields = '__all__'

class TerrainsDeSportsCustomPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerrainsDeSportsCustomPoint
        geo_field = 'geom'
        fields = '__all__'

class ToilettesPubliquesCuyPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ToilettesPubliquesCuyPoint
        geo_field = 'geom'
        fields = '__all__'

class TopologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Topology
        fields = '__all__'

class VoieFerreePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VoieFerreePolyline
        geo_field = 'geom'
        fields = '__all__'

class VoiriesYaoundePointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VoiriesYaoundePoint
        geo_field = 'geom'
        fields = '__all__'

class VoiriesYaoundePolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VoiriesYaoundePolyline
        geo_field = 'geom'
        fields = '__all__'

class WorldFontPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldFontPoint
        geo_field = 'geom'
        fields = '__all__'

class WorldPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldPolyline
        geo_field = 'geom'
        fields = '__all__'

class WorldRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldRegion
        geo_field = 'geom'
        fields = '__all__'

class Z1C121CPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C121CPolyline
        geo_field = 'geom'
        fields = '__all__'

class Z1C122CPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C122CPoint
        geo_field = 'geom'
        fields = '__all__'

class Z1C122CPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C122CPolyline
        geo_field = 'geom'
        fields = '__all__'

class Z1C131CPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C131CPolyline
        geo_field = 'geom'
        fields = '__all__'

class Z1C132CPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C132CPolyline
        geo_field = 'geom'
        fields = '__all__'

class Z1C133CPolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Z1C133CPolyline
        geo_field = 'geom'
        fields = '__all__'

class ZoneAdressageRegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ZoneAdressageRegion
        geo_field = 'geom'
        fields = '__all__'

class ZonesProscritesEllipseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ZonesProscritesEllipse
        geo_field = 'geom'
        fields = '__all__'

