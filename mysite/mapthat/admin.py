from django.contrib import admin
from .models import Marker, Map

# Register your models here.


class MarkerInLine(admin.TabularInline):
    model = Marker


class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_latitude', 'location_longitude', 'zoom')
    inlines = [MarkerInLine]


class MarkerAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'popup',
                    'tooltip', 'color', 'map')
    list_filter = ['map']


admin.site.register(Map, MapAdmin)
admin.site.register(Marker, MarkerAdmin)
