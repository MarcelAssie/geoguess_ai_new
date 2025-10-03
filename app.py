from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # autorise les appels depuis Vue (localhost:5173)

# Exemple de données
adresses = [
    {"id": "id_001", "commune": "Paris", "voie": "Rue de Rivoli", "numero": 25, "lat": 48.8566, "lon": 2.3522},
    {"id": "id_002", "commune": "Paris", "voie": "Avenue des Champs-Élysées", "numero": 50, "lat": 48.8698, "lon": 2.3076},
]

@app.route("/api/adresses", methods=["GET"])
def get_adresses():
    return jsonify(adresses)

if __name__ == "__main__":
    app.run(debug=True)
