import configparser
import os

def get_config():
    config = configparser.ConfigParser()
    os.chdir("..")
    config.read(str(os.getcwd()) + "\\web.conf")
    return config


conf = get_config()

def get_urlpath():

    url = conf.get("rapid_api", "url")
    return conf.get("rapid_api", "protocol") + "://" + str(url) +  \
           "/forecast/3hourly?lat=35.5&lon=-78.5&units=imperial&lang=en"


def get_header():

    headers = {
        "x-rapidapi-host": conf.get("rapid_api", "url"),
        "x-rapidapi-key": conf.get("rapid_api", "api_key")
    }
    return headers

