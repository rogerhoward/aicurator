import simplejson as json
import os

if 'SERVERTYPE' in os.environ and os.environ['SERVERTYPE'] == 'AWS Lambda':
    env_vars = os.environ
else:
    json_data = open('../secrets/aicurator.json')
    env_vars = json.load(json_data)

MICROSOFT_VISION_KEY = env_vars['MICROSOFT_VISION_KEY']
MICROSOFT_ENDPOINT = env_vars['MICROSOFT_ENDPOINT']
TWITTER_CONSUMER_KEY = env_vars['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = env_vars['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN = env_vars['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = env_vars['TWITTER_ACCESS_TOKEN_SECRET']

LOCALES = ['bg_BG', 'fi_FI', 'fr_FR']