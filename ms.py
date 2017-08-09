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

        # Replace the three dots below with the URL of a JPEG image of a celebrity.

        body = json.dumps({'url': self.image})
        # body = "{'url':'" +  + "'}".format(self.image)

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


# this_vision = Vision('http://images.metmuseum.org/CRDImages/ep/web-large/ep89.21.1.R.jpg')
# pprint(this_vision.result)

# print(this_vision.result['description']['captions'][0]['text'].title())