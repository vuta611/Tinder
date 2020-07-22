import tinder_api
import fb_auth_token
import features

host = 'https://api.gotinder.com'
fb_username = 'vu.ta611@gmail.com'
fb_password = 'Anhvu1995'

fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)

tinder_api.get_auth_token(fb_access_token, fb_user_id)

def autolike():
    recs = tinder_api.get_recommendations()#['results']
    if 'results' not in recs:
        tinder_api.update_location(a,b)
        
        autolike()
    else:
        results = recs['results']
        for person in results: 
            person_id = person["_id"]
            name = person["name"]
            print(name)
            tinder_api.like(person_id)
        features.pause()

#'{"message":"recs timeout"}'

while True:
    autolike()