import tinder_api_sms
import features
import random

places = {
    ('10.766869', '106.692811'):'Bui Vien', 
    ('21.035127', '105.851987'):'Ta Hien',
    ('10.782762', '106.696145'):'Ho Con Rua',
    ('10.774283', '106.703114'):'Nguyen Hue',
    ('21.025293', '105.853269'):'Trang Tien',
    ('10.765876', '106.640032'):'Dam Sen',
    ('20.994786', '105.869084'):'Times City',
    ('10.806921', '106.731094'):'Thao Dien'
}

def autolike():
    recs = tinder_api_sms.get_recommendations()
    if 'results' not in recs:
        lat, lon = random.choice(list(places))
        print('Switching to: %s' %(places[lat, lon]))
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