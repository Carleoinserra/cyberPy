print(2 + 4)
print(2 + 5)
# definiamo la funzione somma che dati due parametri stampa la somma didue numeri
def somma(x, y):
    print(x +y)

# invoco la funzione con diversi parametro

somma(120, 4)
somma(45, 2)
somma(5, 8)

somma(int(input("inserisci numero")), int (input("Inserisci numero")))



def stampaNome(x):
    print(x)

stampaNome("Carlo")
stampaNome("Michele")

def prodotto(x, y):
    return x * y

print(prodotto(2, 4))

risultato = prodotto(2, prodotto (2,4))
print(risultato)

