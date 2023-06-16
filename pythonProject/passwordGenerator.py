import random

# Definisci una lista di parole chiave da utilizzare per generare la password
parole_chiave = ["python", "programmazione", "password", "sicurezza", "openai", "intelligenza", "artificiale"]

# Genera una password casuale scegliendo 3 parole chiave a caso dalla lista
password = ""
for i in range(3):
    password += random.choice(parole_chiave)

# Aggiungi un numero casuale alla fine della password
password += str(random.randint(0, 99))

# Aggiungi un carattere speciale casuale alla fine della password
caratteri_speciali = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
password += random.choice(caratteri_speciali)

# Stampa la password generata
print("La tua nuova password è:", password)
