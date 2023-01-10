import pandas as pd
import numpy as np
from . import zipcode_map
import random
from .models import Map, Marker

colormap = {
    'Cornell University': 'darkblue',
}


def makemapzip(file, currmap):
    # Read in the data
    df = pd.read_excel(file)
    # Cut down the data to just the zip codes, popup, and tooltip
    df = df.iloc[:, :3]
    # Rename the Columns: Code, Popup, Tooltip
    df.columns = ['Latlong', 'Popup', 'Tooltip']
    # Convert Zipcodes to Lat/Long List
    df['Latlong'] = df['Latlong'].map(zipcode_map.zipmap)

    # Convert to Records
    records = df.to_records()
    print(records)

    # Add the markers from records
    for record in records:
        marker = Marker(
            latitude=record[1][0],
            longitude=record[1][1],
            popup=record[2],
            tooltip=record[3],
            map=currmap)
        marker.save()
    return currmap


def makemapll(file, currmap):
    # Read in the data
    df = pd.read_excel(file)
    # Cut down the data to just the zip codes, popup, and tooltip
    df = df.iloc[:, :4]
    # Rename the Columns: Lat, Long, Popup, Tooltip
    df.columns = ['Lat', 'Long', 'Popup', 'Tooltip']

    # Convert to Records
    records = df.to_records()

    # Add the markers from records
    for record in records:
        marker = Marker(
            latitude=record[1],
            longitude=record[2],
            popup=record[3],
            tooltip=record[4],
            map=currmap)
        marker.save()
    return currmap
