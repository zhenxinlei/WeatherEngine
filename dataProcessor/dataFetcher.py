from pprint import pprint
import requests

matrix = []

for  ind in range(0,10,1):
    la = 40+0.1*ind
    lo_array = []
    print(la)

    for lo in range(-73, -70, 1):
        la_ = str(la+0.1)
        lo_ = str(lo +1)
        #print('http://api.openweathermap.org/data/2.5/box/city?bbox='+str(lo)+','+str(la)+','+lo_+','+la_+',10&appid=0b74213a07c89ca3278264e0f9618c92')
        r = requests.get('http://api.openweathermap.org/data/2.5/box/city?bbox='+str(lo)+','+str(la)+','+lo_+','+la_+',10&appid=0b74213a07c89ca3278264e0f9618c92')

        json = r.json()
        print("333333")
        pprint(json)

        print("!!!!")
        temp = json['list']

        #[0]['main']['temp']
        #pprint(temp)
        lo_array.append(temp)
        # for list in json['list']:
        #     print(list['name'])
        #     pprint(list['main']['temp'])
        #     print('----------------')
    matrix.append(lo_array)

print(matrix)



print('########ma9##################')
#pprint(json['query']['results']['channel']['item']['condition']['temp'])



# {u'base': u'cmc stations',
#  u'clouds': {u'all': 68},
#  u'cod': 200,
#  u'coord': {u'lat': 51.50853, u'lon': -0.12574},
#  u'dt': 1383907026,
#  u'id': 2643743,
#  u'main': {u'grnd_level': 1007.77,
#            u'humidity': 97,
#            u'pressure': 1007.77,
#            u'sea_level': 1017.97,
#            u'temp': 282.241,
#            u'temp_max': 282.241,
#            u'temp_min': 282.241},
#  u'name': u'London',
#  u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
#  u'weather': [{u'description': u'broken clouds',
#                u'icon': u'04d',
#                u'id': 803,
#                u'main': u'Clouds'}],
#  u'wind': {u'deg': 158.5, u'speed': 2.36}}
