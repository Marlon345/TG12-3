
from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError

app = Flask(__name__)
from model import Spieler
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten