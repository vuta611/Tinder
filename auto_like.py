import tinder_api_sms
import features
import random

locations = {
    '10.766869':'106.692811', 
    '21.035127':'105.851987', 
    '16.065015':'108.221882', 
    '11.947322':'108.440285',
    '10.782762':'106.696145',
    '10.033279':'105.788268'
}

places = {
    ('10.766869', '106.692811'):'Bui Vien', 
    ('21.035127','105.851987'):'Ta Hien',
    ('16.065015', '108.221882'):'Da Nang',
    ('11.947322', '108.440285'):'Da Lat',
    ('10.782762', '106.696145'):'Ho Con Rua',
    ('10.033279', '105.788268'):'Ninh Kieu'
}

def get_places(lat, lon):
    return print('Switching to: %s' %(places[lat, lon]))

def autolike():
    recs = tinder_api_sms.get_recommendations()
    if 'results' not in recs:
        lat, lon = random.choice(list(locations.items()))
        get_places(lat, lon)
        tinder_api_sms.update_location(lat, lon)
        autolike()
    else:
        results = recs['results']
        for person in results: 
            person_id = person["_id"]
            name = person["name"]
            print(name)
            features.pause()
            tinder_api_sms.like(person_id)

while True:
    autolike()