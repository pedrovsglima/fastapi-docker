import requests

URL_BASE = "http://0.0.0.0:8000/"
# endpoint = ""
# endpoint = "teams"
endpoint = "players"
# params = ""
# params = "/LAL"
# params = "/totals"
params = "/3432"
# params = "?abb=LAL&season=2023"
data = {}
# data = {
#     "abb": "SPO",
#     "season": 2024,
#     "team": "SPORT",
# }
# data = {
#     "abb": "LAL",
#     "season": 2023
# }
# data = {
#     "id": 3432,
#     "season": 2004
# }

url = URL_BASE+endpoint+params
print(url)
response = requests.get(url, json=data)
# response = requests.post(url, json=data)
# response = requests.delete(url)

if response.status_code==200:
    print(response.json())
else:
    print(response.status_code)
    print(response.content)