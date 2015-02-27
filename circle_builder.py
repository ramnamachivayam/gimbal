import urllib2
import json

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


def populate_circle():
    for c in range(35780, 50000):
        geo = {
            'shape': 'CIRCLE',
            'radius': 100,
            'center': get_point(),
            'points': [],
            'source': None,
            'sourceId': None,
            'sourceVersion': None
        }
        attributes = {
            GLOBAL_ATTRIBUTE_KEY + 'circle-' + str(c): GLOBAL_ATTRIBUTE_NAME + 'circle-' + str(c)
        }
        data = {
            'name': GLOBAL_NAME_CIRCLE + str(c),
            'geofence': geo,
            'beacons': [],
            'attributes': attributes
        }

        do_send(data, c)

def do_send(data, c):
    #print json.dumps(data)
    response = urllib2.urlopen(get_request(), json.dumps(data))
    print str(c) + '-' + str(response.getcode())

def get_point():
    point = {
        'latitude': 37.7723734,
        'longitude': -122.40571510000001
    }
    return point

if __name__ == '__main__':
    populate_circle()
