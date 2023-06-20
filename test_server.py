import requests

URL_BASE = "http://127.0.0.1:8000/"
# endpoint = ""
# endpoint = "teams/LAL"
endpoint = "teams"
# params = ""
params = "?abb=LAL&season=2023"

url = URL_BASE+endpoint+params
print(url)
response = requests.get(url)

if response.status_code==200:
    print(response.json())
else:
    print(response)