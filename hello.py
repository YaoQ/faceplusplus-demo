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

# In this tutorial, you will learn how to call Face ++ APIs and implement a
# simple App which could recognize a face image in 3 candidates.

api = init() 

# Here are the person names and their face images
IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
PERSONS = [
    ('Jim Parsons', IMAGE_DIR + '1.jpg'),
    ('Leonardo DiCaprio', IMAGE_DIR + '2.jpg'),
    ('Andy Liu', IMAGE_DIR + '3.jpg')
]
TARGET_IMAGE = IMAGE_DIR + '4.jpg'

# Step 1: Detect faces in the 3 pictures and find out their positions and
# attributes

FACES = {name: api.detection.detect(url = url)
        for name, url in PERSONS}

for name, face in FACES.iteritems():
    print_result(name, face)


# Step 2: create persons using the face_id
for name, face in FACES.iteritems():
    rst = api.person.create(
            person_name = name, face_id = face['face'][0]['face_id'])
    print_result('create person {}'.format(name), rst)

# Step 3: create a new group and add those persons in it
rst = api.group.create(group_name = 'standard')
print_result('create group', rst)
rst = api.group.add_person(group_name = 'standard', person_name = FACES.iterkeys())
print_result('add these persons to group', rst)

# Step 4: train the model
rst = api.train.identify(group_name = 'standard')
print_result('train', rst)
# wait for training to complete
rst = api.wait_async(rst['session_id'])
print_result('wait async', rst)

# Step 5: recognize face in a new image
rst = api.recognition.identify(group_name = 'standard', url = TARGET_IMAGE)
print_result('recognition result', rst)
print '=' * 60
print 'The person with highest confidence:', \
        rst['face'][0]['candidate'][0]['person_name']

# Finally, delete the persons and group because they are no longer needed
api.group.delete(group_name = 'standard')
api.person.delete(person_name = FACES.iterkeys())

# Congratulations! You have finished this tutorial, and you can continue
# reading our API document and start writing your own App using Face++ API!
# Enjoy :)
