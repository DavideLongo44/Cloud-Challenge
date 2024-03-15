import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import OperationFailure
from config import mongodb_uri

def extract_and_write_to_mongodb(input_files, mongodb_uri):
    # Inizializza un set vuoto per memorizzare i numeri di telefono unici
    unique_phone_numbers = set()

    # Regular expression pattern to match German phone numbers
    # Espressione regolare per individuare i numeri di telefono tedeschi
    pattern = r'\b(?:\+?49|0049)\s*\d{11}\b'

    # Iterate through all input files
    # Itera attraverso tutti i file di input
    for input_file in input_files:
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
    client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

    # Specify the name of the database in the connection URI
    # Specifica il nome del database nell'URI di connessione
    db_name = "il_tuo_nome_database"

    try:
        # Try to authenticate and perform the insert operation
        # Prova ad autenticarti e a eseguire l'operazione di inserimento
        client.admin.command('ping')
        print("Ping al tuo deployment. Connessione a MongoDB riuscita!")

        # Insert the unique phone numbers into the MongoDB collection
        # Inserisci i numeri di telefono unici nella collezione MongoDB
        for number in unique_phone_numbers:
            client[db_name]["il_tuo_nome_collezione"].insert_one({"phone_number": number})
        
        print("Numeri di telefono inseriti correttamente nel database.")
    except OperationFailure as e:
        print("Errore di autenticazione con MongoDB:", e)

# List of input file names
# Elenco dei nomi dei file di input
input_files = [f'phone_numbers_{i}.txt' for i in range(1, 11)]

# MongoDB connection string (with your password)
# Stringa di connessione MongoDB (con la tua password)


# Esegui l'estrazione dei numeri di telefono e scrivila nel database MongoDB
# Execute the extraction of phone numbers and write it to the MongoDB database
extract_and_write_to_mongodb(input_files, mongodb_uri)
