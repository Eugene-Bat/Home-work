import requests
from config import api_key


def weather(city_name):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}={city_name}'
    x = requests.get(url)
    json = x.json()
    response = f'city/region: {json["location"]["name"]}\nlast update: {json["current"]["last_updated"]}\n' \
               f'Temp(c) = {json["current"]["temp_c"]}\nwind = {json["current"]["wind_kph"]}\n' \
               f'{json["current"]["condition"]["text"]}'
    return response


print(weather('london'))
