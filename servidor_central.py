from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

def cargar_api_keys():
    """
    Carga las claves desde un archivo JSON llamado 'api_keys.json'.
    """
    try:
        with open("api_keys.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo 'api_keys.json'.")
        return []
    except json.JSONDecodeError:
        print("ERROR: El archivo 'api_keys.json' tiene un formato incorrecto.")
        return []

@app.route('/get_keys', methods=['GET'])
def get_keys():
    """
    Este es el único endpoint. Devuelve la lista de claves en formato JSON.
    """
    api_keys = cargar_api_keys()
    print(f"Petición recibida. Entregando {len(api_keys)} claves.")
    return jsonify(api_keys)
