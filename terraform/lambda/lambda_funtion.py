import json
import pymongo
from pymongo import MongoClient
from config import mongodb_uri  # Importa l'URI MongoDB dal file config.py

# Configura la connessione al database MongoDB
def connect_to_mongodb():
    client = MongoClient(mongodb_uri)
    db = client["phone_numbers"]  # Specifica il nome del database
    collection = db["phone_collection"]  # Specifica il nome della collezione
    return collection

# Funzione per gestire una richiesta POST per aggiungere un numero di telefono tedesco al database
def add_phone_number(event, context):
    # Connessione al database MongoDB
    collection = connect_to_mongodb()

    # Estrapola il numero di telefono dal corpo della richiesta
    request_body = json.loads(event["body"])
    phone_number = request_body["phone_number"]

    # Verifica se il numero di telefono è valido
    if is_valid_german_phone_number(phone_number):
        # Inserisci il numero di telefono nel database
        result = collection.insert_one({"phone_number": phone_number})
        response_body = {"message": "Phone number added successfully", "id": str(result.inserted_id)}
        status_code = 200
    else:
        response_body = {"message": "Invalid German phone number"}
        status_code = 400

    # Prepara la risposta HTTP
    response = {
        "statusCode": status_code,
        "body": json.dumps(response_body),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response

# Funzione per verificare se un numero di telefono è valido
def is_valid_german_phone_number(phone_number):
    pattern = r'\b(?:\+?49|0049)\s*\d{11}\b'
    return bool(re.match(pattern, phone_number))

# Funzione per gestire una richiesta GET per recuperare tutti i numeri di telefono
def get_all_phone_numbers(event, context):
    # Connessione al database MongoDB
    collection = connect_to_mongodb()

    # Recupera tutti i numeri di telefono dal database
    phone_numbers = [doc["phone_number"] for doc in collection.find()]

    # Prepara la risposta HTTP
    response = {
        "statusCode": 200,
        "body": json.dumps(phone_numbers),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
