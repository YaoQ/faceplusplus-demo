#!/usr/bin/env python2
# You need to register your App first, and enter you API key/secret.
API_KEY = '29f7e14333edb39f323093704d82e92a'
API_SECRET = 'DXjuFA8gpvvzHaMiOSTZzdh1qZqtmNzq'

# Import system libraries and define helper functions
import time
import sys

from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

# First import the API class from the SDK
from facepp import API
from facepp import File

if len(sys.argv) < 4:
    print 'error!'
    print './add_new_person.py <person_name> <image_path> <group_name>'
    sys.exit()

person_name = sys.argv[1]
path = sys.argv[2]
group_name = sys.argv[3]

api = API(API_KEY, API_SECRET)

result = api.detection.detect(img = File(path))
print_result('Detection result for {}:'.format(person_name), result)
print 'faceid is *************'
print result
face_id = result['face'][0]['face_id'] 
#
## Create a person in the group, and add the face to the person
result = api.person.create(person_name = person_name, face_id = face_id)
#print result
#
result = api.group.add_person(group_name = group_name, person_name = person_name)
#
result = api.train.identify(group_name = group_name)
session_id = result['session_id']
#
result = api.wait_async(session_id)
print result
print 'done!'
