from django.db import models

# Create your models here.

DEFAULT_LATITUDE = 37.8283
DEFAULT_LONGITUDE = -95.5795
DEFAULT_ZOOM = 4.5
DEFAULT_TILES = 'Stamen Terrain'
DEFAULT_ATTR = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'

colorchoices = [
    ('green', 'Green'), ('lightblue', 'Lightblue'), ('pink', 'Pink'),
    ('blue', 'Blue'), ('cadetblue', 'Cadetblue'),
    ('darkpurple', 'Darkpurple'), ('red', 'Red'), ('beige', 'Beige'),
    ('black', 'Black'), ('darkred', 'Darkred'), ('darkgreen', 'Darkgreen'),
    ('gray', 'Gray'), ('lightgray', 'Lightgray'), ('orange', 'Orange'),
    ('lightred', 'Lightred'), ('purple', 'Purple'), ('darkblue', 'Darkblue'),
    ('lightgreen', 'Lightgreen'), ('white', 'White')
]


class Map(models.Model):
    name = models.CharField(max_length=100, default='Default Map')
    location_latitude = models.FloatField(default=DEFAULT_LATITUDE)
    location_longitude = models.FloatField(default=DEFAULT_LONGITUDE)
    zoom = models.FloatField(default=DEFAULT_ZOOM)
    tiles = models.CharField(max_length=255, default=DEFAULT_TILES)
    attr = models.CharField(max_length=500, default=DEFAULT_ATTR)

    def default_map():
        return Map(location_latitude=37.8283, location_longitude=-95.5795, zoom=4.5).pk

    def __str__(self):
        return self.name


class Marker(models.Model):
    popup = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE,
                            default=Map.default_map())
    color = models.CharField(
        max_length=100, default='red', choices=colorchoices)
    tooltip = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.popup
