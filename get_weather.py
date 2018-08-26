# This will fetch the weather. 

import requests, json, sys, argparse


def get_weather_for_city(url,city_id,api_key):
    result = ""
    try:
        r = requests.get(url + "?id=" + city_id + "&APPID=" + api_key)
        if r.status_code != 200:
            print('Error fetching weather from openweathermap.org, status code:' + r.status_code)
        result = r.text
    except Exception as e:
        print(e)
    return result

def parse_result(json_body):
    parse_input = json.loads(json_body)
    return parse_input['city']



parser = argparse.ArgumentParser()
parser.add_argument('--cityid', default='london', help='The city to fetch the weather for', dest="city_id")
parser.add_argument('--apikey', default='123456', help='Your API Key for openweathermap.org', dest="api_key")
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
api_key = args.api_key
city_id = args.city_id

city_input = get_weather_for_city("http://api.openweathermap.org/data/2.5/forecast",city_id,api_key)
parse_city = parse_result(city_input)
print(parse_city)

