import requests
from requests_oauthlib import OAuth1
import json
reload(sys)
sys.setdefaultencoding("utf-8")


params = {'app_key': 'xx',
            'app_secret': 'xx',
            'access_token': 'xx-xx',
            'access_secret': 'xx'}


auth = OAuth1(params['app_key'],
                params['app_secret'],
                params['access_token'],
                params['access_secret'])

                
twittername = 'nameoftwitteraccount'
# Twitter API can only limit by day
since = '2017-09-20' #date


# https://dev.twitter.com/rest/public/search
# note that space, #, etc. have their special percent encoding https://en.wikipedia.org/wiki/Percent-encoding
url_rest = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3A{}&result_type=recent&since%3A{}'.format(twittername, since)


results = requests.get(url_rest, auth=auth)
results = results.json() #convert json into dict
results = json.dumps(results, indent=4) #print pretty, converts to string


with open('text.json', 'wb') as file:
    file.write(results)
    
