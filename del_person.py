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
from facepp import File

if len(sys.argv) < 2:
    print 'error!'
    print 'lost persion_name'
    sys.exit()

person_name = sys.argv[1]

api = API(API_KEY, API_SECRET)

result = api.person.delete(person_name = person_name)
print_result("result is :", result)
print 'done!'
