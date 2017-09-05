import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# Facebook App Token (long live compared to User Token)
fbtoken = 'xx|xx'


# Time Zone
# ----------------------------------------
def timezone(fbdate):
    '''convert utc to local time'''
    a = dateutil.parser.parse(fbdate)
    a = a.replace(tzinfo=tz.tzutc())
    a = a.astimezone(tz.tzlocal())
    a = a.strftime("%Y-%m-%d %I:%M %p")
    return a


# Request
# ----------------------------------------
user = 'name' #name of facebook public account (personal account can't be tapped without their approval)
since = 1504624172 #epoch time
req = '{}/posts?fields=permalink_url,message,story,created_time,updated_time&limit=50&until=now&since={}'.format(user, since)
r = requests.get('https://graph.facebook.com/v2.10/{}'.format(req), params={'access_token':fbtoken}) #set request


data = r.json()
print json.dumps(data, indent=4)

