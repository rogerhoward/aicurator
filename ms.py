#!/usr/bin/env python
import config
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from pprint import pprint

class Vision(object):

    def __init__(self, image):
        self.image = image
        self.recognize()

    def recognize(self):

        headers = {
            # Request headers.
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': config.MICROSOFT_VISION_KEY,
        }

        params = urllib.parse.urlencode({
            # Request parameters. All of them are optional.
            'visualFeatures': 'Categories,Description,Color',
            'language': 'en',
        })

        body = json.dumps({'url': self.image})

        try:
            # Execute the REST API call and get the response.
            conn = http.client.HTTPSConnection(config.MICROSOFT_ENDPOINT)
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            self.result = json.loads(data)

        except Exception as e:
            print('Error:')
            print(e)

