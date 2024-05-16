import urllib.request
import json
import os


def get_weather(city):
  # API key
  api = os.environ['weather_api']
  # Base URL
  url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
  # Request
  request = urllib.request.urlopen(url)
  # Result
  result = json.loads(request.read())

  
  return result