import re
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from config import mongodb_uri

def extract_and_write_to_mongodb(input_file, mongodb_uri):
    
    # Initialize an empty set to store unique phone numbers
    # Inizializza un set vuoto per memorizzare i numeri di telefono unici
    unique_phone_numbers = set()

    # Regular expression pattern to match German phone numbers
    # Espressione regolare per individuare i numeri di telefono tedeschi
    pattern = r'\b(?:\+?49|0049)\s*\d{11}\b'

    # Read the content of the input file
    # Leggi il contenuto del file di input
    with open(input_file, 'r') as f:
        content = f.read()

    # Find all valid German phone numbers in the content
    # Trova tutti i numeri di telefono tedeschi validi nel contenuto
    phone_numbers = re.findall(pattern, content)
        
    # Add the extracted phone numbers to the set
    # Aggiungi i numeri di telefono estratti al set
    unique_phone_numbers.update(phone_numbers)

    # Connect to MongoDB using the connection URI
    # Connetti a MongoDB usando l'URI di connessione
    client = MongoClient(mongodb_uri)

    # Specify the name of the database
    # Specifica il nome del database
    db_name = "phone_numbers"

    try:
        # Try to authenticate and perform the insert operation
        # Prova ad autenticarti e a eseguire l'operazione di inserimento
        client.admin.command('ping')
        print("Ping to your deployment. Connection to MongoDB successful!")

        # Insert the unique phone numbers into the MongoDB collection
        # Inserisci i numeri di telefono unici nella collezione MongoDB
        for number in unique_phone_numbers:
            # Check if the phone number starts with "+49" or "0049"
            # Verifica se il numero di telefono inizia con "+49" o "0049"
            if number.startswith("+49") or number.startswith("0049"):
                client[db_name]["phone_collection"].insert_one({"phone_number": number})
        
        print("Phone numbers inserted successfully into the database.")
    except OperationFailure as e:
        print("Error authenticating with MongoDB:", e)

# Name of the input file
# Nome del file di input
input_file = "all_phone_numbers.txt"

# Execute the extraction of phone numbers and write it to the MongoDB database
# Esegui l'estrazione dei numeri di telefono e scrivi nel database MongoDB
extract_and_write_to_mongodb(input_file, mongodb_uri)
