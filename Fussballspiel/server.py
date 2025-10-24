
from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError
import json
import os

app = Flask(__name__)
from model import Spieler
spielerliste = []

# Route für die Hauptseite
@app.route('/')
def home():
    return "Server ist bereit und wartet auf Anfragen."

# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    response_message = f"Echo: {message}"
    return jsonify({"response": response_message})

@app.route('/spieler', methods=['POST'])
def handle_Spieler():
    #Erstellt einen neuen Spieler aus den Bekommenden Daten von client2
    try:
        data = request.get_json()
        spieler = Spieler(**data)
        spielerliste.append(spieler)
        print(spieler.model_dump_json)
        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt",
            "Spieler": spieler.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen"
        }), 400

def loaddata(spielerJson):
    if os.path.exists(spielerJson):
        print("hell yeahh")
        with open(spielerJson, "r", encoding="utf-8") as f:
            daten = json.load(f)
            spielerliste = [Spieler(**s) for s in daten]
            print("📂 Geladene Spieler:")
            for s in spielerliste:
                print(s)
    else:
        print(f"⚠️ Datei '{spielerJson}' wurde nicht gefunden.")
        print("Es wird eine leere Spielerliste erstellt.")
        spielerliste = []

if __name__ == '__main__':
        loaddata("spieler.json")

        app.run(host='0.0.0.0', port=12345)  # Server starten
        
        with open("spieler.json", "w", encoding="utf-8") as f:
            json.dump([s.model_dump() for s in spielerliste], f, ensure_ascii=False, indent=4)
        print("✅ Spieler wurden in 'spieler.json' gespeichert.")
        


       

