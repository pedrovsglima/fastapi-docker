import requests

URL_BASE = "http://127.0.0.1:8000"

response = requests.get(f"{URL_BASE}/teams/ATL")

if response.status_code==200:
    print(response.json())
else:
    print(response)