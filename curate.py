#!/usr/bin/env python

import config, ms, twit
from pprint import pprint
from faker import Factory
import random
import simplejson as json

art_data = json.load(open('art.json'))


fake = Factory.create(random.choice(config.LOCALES))

image_url = random.choice(art_data['art'])
image_url = art_data['art'][2]

this_vision = ms.Vision(image_url)

image_title = this_vision.result['description']['captions'][0]['text'].title()

artist_name = fake.name()

tombstone = '"{}", by {}'.format(image_title, artist_name)
print(tombstone)

pprint(config.env_vars)


this_tweet = twit.Tweet(tombstone, image_url)