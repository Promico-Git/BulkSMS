import urllib.request
import json

def get_spaceInfo():
  url = f"http://api.open-notify.org/astros.json"

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  return result