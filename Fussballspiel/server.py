from flask import Flask, request, jsonify
from model import Spieler
app = Flask(__name__)

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

@app.route('/student"', methods=['POST'])

@app.route("/student", methods=["GET"])
def send_student():
    s = Spieler(name="Jan", position="Sturm", motivation="10")
    return jsonify(s.model_dump())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten