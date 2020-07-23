import tinder_api_sms
import features
import random

places = {
    ('10.766869', '106.692811'):'Bui Vien', 
    ('21.035127', '105.851987'):'Ta Hien',
    ('16.065015', '108.221882'):'Da Nang',
    ('11.947322', '108.440285'):'Da Lat',
    ('10.782762', '106.696145'):'Ho Con Rua',
    ('10.033279', '105.788268'):'Ninh Kieu',
    ('20.855117', '106.682231'):'Hai Phong'
}

def get_places(lat, lon):
    return print('Switching to: %s' %(places[lat, lon]))

def autolike():
    recs = tinder_api_sms.get_recommendations()
    if 'results' not in recs:
        lat, lon = random.choice(list(places))
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