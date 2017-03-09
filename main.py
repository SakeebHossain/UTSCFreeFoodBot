import requests
import simplejson as json
from access_tokens import APP_ID
from access_tokens import SECRET_KEY 
from access_tokens import GROUP_ID 

# Using the format specified on this page https://developers.facebook.com/docs/facebook-login/access-tokens/
# under "App Access Tokens"
access_token = APP_ID + "|" + SECRET_KEY
url = "https://graph.facebook.com/" + GROUP_ID + "/feed?access_token=" + access_token

# Retrieve JSON response.
res = requests.get(url)
json_posts = json.loads(str(res.text))
