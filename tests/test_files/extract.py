#import regular expression
import re

def extract_phone_numbers(input_files, output_file):
    # Inizializza un insieme vuoto per memorizzare i numeri di telefono unici
    # Initialize an empty set to store unique phone numbers
    unique_phone_numbers = set()

    # Itera attraverso tutti i file di input
    # Iterate through all input files
    for input_file in input_files:
        # Leggi il contenuto del file di input
        # Read the content of the input file
        with open(input_file, 'r') as f:
            content = f.read()

        # Utilizza una regex per trovare tutti i numeri di telefono validi nel contenuto
        # Use a regex to find all valid phone numbers in the content
        phone_numbers = re.findall(r'\b(?:\+?49|0049)(?:\s*\d){11}\b', content)
        
        # Rimuovi gli spazi da ciascun numero di telefono e aggiungilo all'insieme
        # Remove spaces from each phone number and add it to the set
        for number in phone_numbers:
            number = number.replace(' ', '')  # Rimuovi gli spazi
            unique_phone_numbers.add(number)

    # Scrivi tutti i numeri di telefono unici nel file di output, ordinati
    # Write all unique phone numbers to the output file, sorted
    with open(output_file, 'w') as f:
        for number in sorted(unique_phone_numbers):
            f.write(number + '\n')

# Lista dei nomi dei file di input
# List of input file names
input_files = [f'phone_numbers_{i}.txt' for i in range(1, 11)]

# Nome del file di output
# Name of the output file
output_file = 'all_phone_numbers.txt'

# Estrai tutti i numeri di telefono unici, formattali e ordinali, quindi scrivili in un singolo file di output
# Extract all unique phone numbers, format and sort them, then write to a single output file
extract_phone_numbers(input_files, output_file)
