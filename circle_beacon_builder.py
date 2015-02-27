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

def populate_circle_beacon():
    for i in range(11295, 25000):
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
            GLOBAL_ATTRIBUTE_KEY + 'circle-beacon-' + str(i): GLOBAL_ATTRIBUTE_NAME + 'circle-beacon-' + str(i)
        }

        beacons = get_beacons_list()

        data = {
            'name': GLOBAL_NAME_CIRCLE_BEACON + str(i),
            'geofence': geo,
            'beacons': beacons,
            'attributes': attributes
        }

        do_send(data, i)

def do_send(data, i):
    #print json.dumps(data)
    response = urllib2.urlopen(get_request(), json.dumps(data))
    print str(i) + '-' + str(response.getcode())

#@staticmethod
def get_beacons_list():
    beacons = []
    beacon_size = randint(1, 9) + 1
    for m in range(0, beacon_size):
        beacons.append(get_beacon_list()[m])
    return beacons

def get_point():
    point = {
        'latitude': 37.7723734,
        'longitude': -122.40571510000001
    }
    return point


#@staticmethod
def get_beacon_list():
    b1 = {'id': '9B78C5EF883A4F6CA9009834822323E2', 'name': 'Kellogg Test 2'}
    b2 = {'id': 'F8F3616CDA2D49D396A32F6DADAAE1EC', 'name': 'test today'}
    b3 = {'id': 'CE588D5408914740B5011583CD19BB2D', 'name': 'Test iBeacon 1'}

    b4 = {'id': '5FC966C484BB4E8791598E9907B3121B', 'name': 'Kellogg Test 1'}
    b5 = {'id': '9F04EE6CD32E46E79599BD73B6F270AE', 'name': 'Voyager Test Beacon'}
    b6 = {'id': 'A683C47052D64EE4910462130120F05B', 'name': 'XenoZone Test Beacon2'}

    b7 = {'id': '5D38A9BD83264D0CA27396164A5924B7', 'name': 'Domino Test Beacon'}
    b8 = {'id': '48A0D24F7B404954A2EEFCDB605263C8', 'name': 'Sashi Test 101'}
    b9 = {'id': '9E6DBB5FCE4C4488B56D147FFF5693E6', 'name': 'RS Test Beacon 1'}

    b10 = {'id': '838E9FA80B2240A1A9A94DC13675FA84', 'name': 'Test Beacon 2'}

    beacon_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
    return beacon_list

if __name__ == '__main__':
    populate_circle_beacon()