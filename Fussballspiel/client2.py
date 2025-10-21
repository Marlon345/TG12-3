import requests
from model import Spieler
import json
# Server-URL
server_url = 'http://localhost:12345/spieler'
spieler_daten= {
    "name": "Jan",
    "position": "Stürmer",
    "motivation": 10
}

def start():
    name = input("Spieler Name: ")
    position = input("Spieler Position: ")
    motivation = input("Spieler Motivation: ")
    s = Spieler(name=name,position=position,motivation=motivation)
    response = requests.post(server_url, json=s.model_dump())
    print("Statuscode", response.status_code)

    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


while True:
    start()