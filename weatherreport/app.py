import requests
from python.weatherreport.util import lib

def get_weather_report():
    response = requests.get(url=lib.get_urlpath(), headers=lib.get_header())
    if response.status_code == 200:
        data = response.json()
        print(data)

get_weather_report()