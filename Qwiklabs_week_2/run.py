#! /usr/bin/env python3

#import necessary python modules
import os
import requests

#Variable declaration
path = '/data/feedback/'
myLink = 'http://<External-IP-Address>/feedback/'
myFiles = os.listdir(path)
keys = ["title", "name", "date", "feedback"]

#Enter for-loop to process files
for file in myFiles:
        #Open files and process data within
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post(myLink,json=fb)

print(response.request.body)
print(response.status_code)

