#!/usr/bin/env python

import twitter
import config


class Tweet(object):
    def __init__(self, text, image):
        self.text = text
        self.image = image
        self.api = twitter.Api(consumer_key=config.TWITTER_CONSUMER_KEY, consumer_secret=config.TWITTER_CONSUMER_SECRET, access_token_key=config.TWITTER_ACCESS_TOKEN, access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET)

        self.send()

    def send(self):
        self.status = self.api.PostMedia(status=self.text, media=self.image)
