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

if len(sys.argv) < 2:
    print 'error!'
    print 'What group name do you want to create?'
    sys.exit()

group_name = sys.argv[1]

api = init() 
result = api.group.create(group_name = group_name)
print 'done!'
