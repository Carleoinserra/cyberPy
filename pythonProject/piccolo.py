
scelta = int(input("Inserisci un numero"))
numpiccolo = scelta
while scelta != 0:

    if scelta < numpiccolo:
        numpiccolo = scelta
    scelta = int(input("Inserisci un numero"))
print(numpiccolo)