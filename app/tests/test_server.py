import requests

URL_BASE = "http://127.0.0.1:8000/"
# endpoint = ""
endpoint = "teams/LAL"
# endpoint = "teams"
params = ""
# params = "?abb=LAL&season=2023"
# params = "?name=SPORT&abb=SPO&season=2024"

url = URL_BASE+endpoint+params
print(url)
# response = requests.get(url)
# response = requests.post(url)
response = requests.delete(url)

if response.status_code==200:
    print(response.json())
else:
    print(response.content)