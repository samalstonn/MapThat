import folium
from django.shortcuts import get_object_or_404
from .models import Marker, Map


def makemap(map, icon):
    folmap = folium.Map(location=[map.location_latitude, map.location_longitude], zoom_start=map.zoom,
                        tiles=map.tiles,
                        attr=map.attr)

    for m in map.marker_set.all():
        marker = folium.Marker(
            location=[m.latitude, m.longitude], popup=m.popup, icon=icon, tooltip=m.tooltip)
        folmap.add_child(marker)
    return folmap
