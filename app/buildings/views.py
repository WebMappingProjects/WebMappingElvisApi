from rest_framework import views, permissions
from rest_framework.response import Response
from django.db.models import Count, Avg
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.apps import apps
import statistics  # Module Python standard

class ServiceStatisticsView(views.APIView):
    """
    Vue pour obtenir le nombre de données enregistrées pour chaque service
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        statistics_data = {}
        
        # Liste des modèles de services principaux
        service_models = {
            # Éducation
            'Écoles maternelles': 'EnseignementMaternelleCustomPoint',
            'Écoles primaires': 'EcolesMatPrimairePoint',
            'Écoles de base': 'EnseignementDeBaseFontPoint',
            'Enseignement primaire': 'EnseignementPrimaireFontPoint',
            'Enseignement secondaire': 'EnseignementsSecondairesFinalPoint',
            'Enseignement supérieur': 'EnseignementSuperieurCustomPoint',
            'École normale': 'EcoleNormaleDesInstituteursDenseignementGeneralPoint',

            # Santé
            'Hôpitaux et centres de santé': 'SanitaireYaoundePoint',
            'Pharmacies': 'PharmaciesPoint',

            # Services financiers
            'Banques et microfinances': 'BanquesEtMicrofinancesCustomPoint',

            # Hôtellerie et restauration
            'Hôtels': 'HotelsFontPoint',
            'Restaurants': 'RestaurantsYaoundeFontPoint',
            'Auberges': 'AubergesCustomPoint',

            # Commerce
            'Marchés': 'MarchesPoint',
            'Marchés communaux': 'MarchesCommunauxCuyPoint',
            'Boulangeries': 'BoulangeriesCustomPoint',

            # Sécurité et forces de l'ordre
            'Commissariats': 'CommissariatsYdeFontPoint',
            'Gendarmeries': 'GendarmeriesPoint',
            'Sapeurs-pompiers': 'SapeursPompierPoint',
            'Camp SIC': 'CampSicCustomPoint',
            'Armée': 'ArmeeFontPoint',

            # Lieux de culte
            'Églises catholiques': 'EglisesCatholiquesFontPoint',
            'Églises presbytériennes': 'EglisesPresbyteriennesFontPoint',
            'Églises protestantes': 'EglisesProtestantesPoint',
            'Mosquées': 'MosqueesFontPoint',
            'Religions (tous)': 'ReligionsYaoundeFontPoint',

            # Culture et loisirs
            'Centres culturels': 'CentresCulturelsCustomPoint',
            'Complexes sportifs': 'ComplexesSportifsCustomPoint',
            'Terrains de sports': 'TerrainsDeSportsCustomPoint',
            'Cinémas': 'CinemaCustomPoint',
            'Radio': 'RadioYaoundeCustomPoint',

            # Services automobiles
            'Garages': 'GaragesCustomPoint',
            'Stations service': 'StationsSevicesFontPoint',

            # Transport
            'Agences de voyage': 'AgencesDeVoyagesFontPoint',
            'Gares routières': 'GaresRoutieresCuyPoint',
            'Gare ferroviaire': 'GareFerrroviaireCustomPoint',
            'Bacs': 'BacsPoint',

            # Institutions et administration
            'Ambassades': 'AmbassadesPoint',
            'Consulats': 'ConsulatsPoint',
            'Nations Unies': 'NationsUniesPoint',
            'Ministères': 'MinisteresYaoundeCustomPoint',
            'Mairies': 'MairiesYaoundeCustomPoint',
            'Préfectures et sous-préfectures': 'PrefecturesSousPrefecturesCustomPoint',
            'Délégations': 'DelegationsCustomPoint',
            'Centre spécial état civil': 'CentreSpecialDetatCivilFontPoint',

            # Services juridiques
            'Huissiers': 'HussiersYdeCustomPoint',

            # Services publics
            'Services municipaux': 'ServicesCuyPoint',
            'Toilettes publiques': 'ToilettesPubliquesCuyPoint',
            'Cités municipales': 'CitesMunicipalesCuyPoint',
            'Bouches incendie': 'BouchesIncendiesYdePoint',

            # Autres services
            'Laveries': 'LaveriesFontPoint',
            'Lieux remarquables': 'LieuxRemarquablesPoint',
        }
        
        for service_name, model_name in service_models.items():
            try:
                model = apps.get_model('buildings', model_name)
                count = model.objects.count()
                statistics_data[service_name] = count
            except:
                statistics_data[service_name] = 0
        
        # Calcul du total
        total = sum(statistics_data.values())
        
        return Response({
            'services': statistics_data,
            'total': total
        })


class GroupedDataView(views.APIView):
    """
    Vue pour regrouper les données en fonction d'une colonne
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        model_name = request.query_params.get('model')
        group_by = request.query_params.get('group_by')
        
        if not model_name or not group_by:
            return Response({
                'error': 'Paramètres requis: model et group_by'
            }, status=400)
        
        try:
            model = apps.get_model('buildings', model_name)
            
            # Vérifier si le champ existe
            if not hasattr(model, group_by):
                return Response({
                    'error': f'Le champ {group_by} n\'existe pas dans le modèle {model_name}'
                }, status=400)
            
            # Effectuer le regroupement
            results = model.objects.values(group_by).annotate(
                count=Count('id')
            ).order_by('-count')
            
            # Calculer le total
            total = sum(item['count'] for item in results)
            
            return Response({
                'model': model_name,
                'grouped_by': group_by,
                'results': results,
                'total': total
            })
            
        except LookupError:
            return Response({
                'error': f'Modèle {model_name} non trouvé'
            }, status=404)


class AverageDistanceView(views.APIView):
    """
    Vue pour calculer la distance moyenne entre les services de même type
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        model_name = request.query_params.get('model')
        limit = int(request.query_params.get('limit', 100))
        
        if not model_name:
            return Response({
                'error': 'Paramètre requis: model'
            }, status=400)
        
        try:
            model = apps.get_model('buildings', model_name)
            
            # Vérifier si le modèle a un champ géométrique
            if not hasattr(model, 'geom'):
                return Response({
                    'error': f'Le modèle {model_name} n\'a pas de champ géométrique'
                }, status=400)
            
            points = model.objects.filter(geom__isnull=False)[:limit]
            
            print(f'Nombre de points récupérés: {points.count()}')
            if points.count() < 2:
                return Response({
                    'error': 'Pas assez de points pour calculer une distance moyenne'
                }, status=400)
            
            distances = []
            srid = None
            # Déterminer le SRID courant (on suppose que tous les points ont le même)
            for pt in points:
                if pt.geom:
                    srid = pt.geom.srid
                    break
            if srid is None:
                return Response({'error': 'Impossible de déterminer le SRID des géométries'}, status=400)
            # Calculer les distances entre chaque paire de points
            for i, point1 in enumerate(points):
                for point2 in points[i+1:]:
                    if point1.geom and point2.geom:
                        try:
                            geom1 = point1.geom
                            geom2 = point2.geom
                            # Si SRID 4326, transformer en 32632 pour calculer en mètres
                            if geom1.srid == 4326:
                                geom1 = geom1.transform(32632, clone=True)
                            if geom2.srid == 4326:
                                geom2 = geom2.transform(32632, clone=True)
                            distance = geom1.distance(geom2)
                            distances.append(distance)
                        except Exception as e:
                            continue
            if not distances:
                return Response({
                    'error': 'Impossible de calculer les distances'
                }, status=400)
            # Calculer les statistiques avec le module statistics de Python
            avg_distance = statistics.mean(distances)
            min_distance = min(distances)
            max_distance = max(distances)
            median_distance = statistics.median(distances)
            return Response({
                'model': model_name,
                'nombre_points_analysés': points.count(),
                'nombre_paires': len(distances),
                'distances': distances,
                'distance_moyenne_metres': round(avg_distance, 2),
                'distance_minimale_metres': round(min_distance, 2),
                'distance_maximale_metres': round(max_distance, 2),
                'distance_mediane_metres': round(median_distance, 2),
                'srid_utilisé': srid,
                'message': f'En moyenne, il faut parcourir {round(avg_distance, 2)} mètres pour trouver un autre {model_name}'
            })
        except LookupError:
            return Response({
                'error': f'Modèle {model_name} non trouvé'
            }, status=404)
        except Exception as e:
            return Response({
                'error': f'Erreur lors du calcul: {str(e)}'
            }, status=500)


class NearestServiceView(views.APIView):
    """
    Vue pour trouver les services les plus proches d'un point donné
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        model_name = request.query_params.get('model')
        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('lon')
        limit = int(request.query_params.get('limit', 5))
        
        if not all([model_name, latitude, longitude]):
            return Response({
                'error': 'Paramètres requis: model, lat, lon'
            }, status=400)
        
        try:
            model = apps.get_model('api', model_name)
            point = Point(float(longitude), float(latitude), srid=4326)
            
            # Transformer en SRID 32632 (utilisé par les données)
            point.transform(32632)
            
            # Trouver les services les plus proches
            nearest = model.objects.filter(
                geom__isnull=False
            ).annotate(
                distance=Distance('geom', point)
            ).order_by('distance')[:limit]
            
            results = []
            for item in nearest:
                result = {
                    'id': item.id,
                    'distance_metres': round(item.distance.m, 2),
                }
                
                # Ajouter les champs informatifs selon le modèle
                if hasattr(item, 'nom'):
                    result['nom'] = item.nom
                elif hasattr(item, 'noms'):
                    result['nom'] = item.noms
                elif hasattr(item, 'etablissem'):
                    result['nom'] = item.etablissem
                
                if hasattr(item, 'quartier'):
                    result['quartier'] = item.quartier
                
                if hasattr(item, 'telephone'):
                    result['telephone'] = item.telephone
                elif hasattr(item, 't_l_phone'):
                    result['telephone'] = item.t_l_phone
                
                results.append(result)
            
            return Response({
                'model': model_name,
                'point_reference': {
                    'latitude': latitude,
                    'longitude': longitude
                },
                'services_proches': results
            })
            
        except LookupError:
            return Response({
                'error': f'Modèle {model_name} non trouvé'
            }, status=404)
        except Exception as e:
            return Response({
                'error': f'Erreur lors de la recherche: {str(e)}'
            }, status=500)