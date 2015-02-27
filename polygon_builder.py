import urllib2
import json
from random import randint

GLOBAL_NAME_CIRCLE = 'load-test-org-2-UrbanAirship-Circle-'
GLOBAL_NAME_POLYGON = 'load-test-org-2-UrbanAirship-Polygon-'
GLOBAL_NAME_CIRCLE_BEACON = 'load-test-org-2-UrbanAirship-Circle-Beacon-'
GLOBAL_NAME_POLYGON_BEACON = 'load-test-org-2-UrbanAirship-Polygon-Beacon-'
GLOBAL_NAME_NO_GEO_BEACON = 'load-test-org-2-UrbanAirship-No-Geo-Beacon-'
GLOBAL_ATTRIBUTE_KEY = 'org-2-key-'
GLOBAL_ATTRIBUTE_NAME = 'org-2-value-'


def get_request():
    req = urllib2.Request('https://manager.gimbal.com/api/v2/places')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.add_header('AUTHORIZATION', 'Token token=770ed07dfecaed8691324fc38385bdde')
    return req

def populate_polygon():
    for i in range(27593, 50000):
        points = get_points()

        geo = {
            'shape': 'POLYGON',
            'radius': None,
            'center': None,
            'points': points,
            'source': None,
            'sourceId': None,
            'sourceVersion': None
        }
        attributes = {
            GLOBAL_ATTRIBUTE_KEY + 'polygon-' + str(i): GLOBAL_ATTRIBUTE_NAME + 'polygon-' + str(i)
        }
        data = {
            'name': GLOBAL_NAME_POLYGON + str(i),
            'geofence': geo,
            'beacons': [],
            'attributes': attributes
        }

        do_send(data, i)

def do_send(data, i):
    #print json.dumps(data)
    response = urllib2.urlopen(get_request(), json.dumps(data))
    print str(i) + '-' + str(response.getcode())

def get_points():
    points = []
    size = randint(1, 5) + 4
    for k in range(0, size):
        points.append(get_point())
    return points

#@staticmethod
def get_point():
    point = {
        'latitude': 37.7723734,
        'longitude': -122.40571510000001
    }
    return point

if __name__ == '__main__':
    populate_polygon()