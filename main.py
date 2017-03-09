import requests
import simplejson as json
from access_tokens import APP_ID
from access_tokens import SECRET_KEY 
from access_tokens import GROUP_ID 
# Using the format specified on this page https://developers.facebook.com/docs/facebook-login/access-tokens/
# under "App Access Tokens"
api_id = APP_ID
secret_key = SECRET_KEY
access_token = api_id + "|" + secret_key

#url = "https://graph.facebook.com/" + GROUP_ID + "/feed?https://graph.facebook.com/search?q=utsc2018&type=group&access_token=" + access_token

url = "https://graph.facebook.com/" + GROUP_ID + "/feed?access_token=" + access_token

res = requests.get(url)
json_posts = json.loads(str(res.text))
print(json_posts)

