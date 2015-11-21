#!/usr/bin/env python2
# Import system libraries and define helper functions
import time
import sys
import os
import os.path
from pprint import pformat

# First import the API class from the SDK
from facepp import API
from facepp import File

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

def init():
    fdir = os.path.dirname(__file__) 
    with open(os.path.join(fdir, 'apikey.cfg')) as f:
        exec(f.read())

    srv = locals().get('SERVER')
    return API(API_KEY, API_SECRET, srv = srv)

if len(sys.argv) < 4:
    print 'error!'
    print './add_new_person.py <person_name> <image_path> <group_name>'
    sys.exit()

person_name = sys.argv[1]
path = sys.argv[2]
group_name = sys.argv[3]

api = init() 

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
