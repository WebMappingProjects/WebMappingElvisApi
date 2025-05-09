from django.contrib import admin
from buildings.models import *
from leaflet.admin import LeafletGeoAdmin # type: ignore
# Register your models here.

# class BuildingAdmin(LeafletGeoAdmin):
#     model = Building

# class PlaceAdmin(LeafletGeoAdmin):
#     model = Place



# class RoadAdmin(LeafletGeoAdmin):
#     model = Road


# admin.site.register(Building, BuildingAdmin)
# admin.site.register(Place, PlaceAdmin)
# admin.site.register(Road, RoadAdmin)

