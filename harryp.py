import urllib.request
import json


def get_character():
 
  # Base URL
  url= f'https://hp-api.onrender.com/api/characters'
  # Request
  request = urllib.request.urlopen(url)
  # Result
  result = json.loads(request.read())

  return result