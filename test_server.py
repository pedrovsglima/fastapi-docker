import requests

URL_BASE = "http://127.0.0.1:8000/"
# endpoint = ""
endpoint = "teams/LAL"

response = requests.get(URL_BASE+endpoint)

if response.status_code==200:
    print(response.json())
else:
    print(response)