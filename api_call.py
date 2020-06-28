import requests
import json

def execute():
  requestUrl = "https://api.nytimes.com/svc/archive/v1/2020/6.json?api-key=<API_key>"
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  with open('nyt_jun.txt', 'w') as outfile:
    json.dump(request.json(), outfile)
  print(request.json())

if __name__ == "__main__":
  execute()
