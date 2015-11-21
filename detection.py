#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: hello.py

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

if len(sys.argv) < 2:
    print 'where is your image path'
    sys.exit()

path = sys.argv[1]

api = API(API_KEY, API_SECRET)

result = api.detection.detect(img = File(path))
print_result('Detection result for {}:', result)
