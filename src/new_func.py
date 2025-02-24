import requests
from dotenv import dotenv_values
from api_key import api_key, api_key_geocode
config = dotenv_values()

server_address = 'https://static-maps.yandex.ru/v1?'
server_address_geocoder = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = api_key
api_key_geocode = api_key_geocode
my_path = 'data/map.png'


def requesting(dolgota, shirota, oblast, metka_bool=False, theme='light'):
    if metka_bool:
        ll_spn = f'll={dolgota},{shirota}&spn={oblast[0]},{oblast[1]}&theme={theme}&pt={dolgota},{shirota}'
    else:
        ll_spn = f'll={dolgota},{shirota}&spn={oblast[0]},{oblast[1]}&theme={theme}'
    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)

    if response.status_code == 200:
        global my_path
        map_file = "data/map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        my_path = 'data/map.png'
        return True
    else:
        print(response.status_code, response.reason)
        return False


def geocode_requesting(geocode, oblast, theme='light'):
    data = f'geocode={api_key_geocode}'
    map_request = f"{server_address_geocoder}{data}&apikey={api_key_geocode}"
    response = requests.get(map_request)

    if response.status_code == 200:
        global my_path
        a = response.text()
        dolgota, shirota = a['response']["featureMember"]["GeoObject"]["Point"]["pos"].split()
        dolgota = float(dolgota)
        shirota = float(shirota)
        requesting(dolgota, shirota, oblast, metka_bool=True, theme=theme)
        return True
