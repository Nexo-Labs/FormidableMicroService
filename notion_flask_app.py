import json
import os
from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Configura tus credenciales y detalles de la base de datos
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
DATABASE_ID = os.environ.get('DATABASE_ID')

# URL de la API de Notion
url = "https://api.notion.com/v1/pages"

# Cabeceras para la solicitud
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"  # Asegúrate de usar la versión más reciente
}

@app.route('/add_record', methods=['POST'])
def add_record_to_notion():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({"error": "Se requiere el campo 'title'"}), 400

    notion_data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": data['title']
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(url, headers=headers, json=notion_data)
    
    if response.status_code == 200:
        return jsonify({"message": "Registro agregado exitosamente a Notion"}), 200
    else:
        return jsonify({"error": f"Error al agregar registro: {response.status_code}", "details": response.text}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)