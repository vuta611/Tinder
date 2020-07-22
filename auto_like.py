import tinder_api_sms
import features
import random

locations = {'10.766869':'106.692811', '21.035127':'105.851987', '16.065015':'108.221882', '11.947322':'108.440285'}
#10.766869, 106.692811 - BV
#21.035127, 105.851987 - TH
#16.065015, 108.221882 - DN
#11.947322, 108.440285 - DL

def autolike():
    recs = tinder_api_sms.get_recommendations()
    if 'results' not in recs:
        lat, lon = random.choice(list(locations.items()))
        tinder_api_sms.update_location(lat, lon)
        autolike()
    else:
        results = recs['results']
        for person in results: 
            person_id = person["_id"]
            name = person["name"]
            print(name)
            tinder_api_sms.like(person_id)
        features.pause()

while True:
    autolike()