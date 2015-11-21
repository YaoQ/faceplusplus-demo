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

api = API(API_KEY, API_SECRET)

if len(sys.argv) < 3:
    print 'error!'
    print './recognize.py <group_name> <image_path>'
    sys.exit()

group = sys.argv[1]
IMAGE_DIR = sys.argv[2] 

rst = api.recognition.identify( group_name = group,img = File(IMAGE_DIR))
#print 'The person with highest confidence:', \
#      rst['face'][0]['candidate'][0]['person_name']
if rst['face']:
    print 'The person with highest confidence:', \
        rst['face'][0]['candidate'][0]['person_name']
    print 'Confidence is :',\
	rst['face'][0]['candidate'][0]['confidence']
else:
   print 'There is no face that is detected!'
