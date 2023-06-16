def calcola_valuta_futura(capitale, tasso_interesse, anni):
    valuta_futura = capitale * (1 + tasso_interesse)**anni
    return valuta_futura

# Input dell'utente
capitale_iniziale = float(input("Inserisci l'importo iniziale di capitale: "))
tasso_interesse_annuo = float(input("Inserisci il tasso di interesse annuo (in decimali): "))
anni = int(input("Inserisci il numero di anni: "))

# Calcola il valore futuro della valuta
valuta_futura = calcola_valuta_futura(capitale_iniziale, tasso_interesse_annuo, anni)

# Stampa il risultato
print("Il valore futuro della valuta dopo", anni, "anni sarà di", valuta_futura)