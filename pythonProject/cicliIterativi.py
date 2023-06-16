



lista = list()
scelta =int(input("quante volte deve iterare"))
somma =0
while scelta > 0:
    numero = int(input("inserisci un numero"))
    lista.append(numero)
    somma += numero
    scelta -= 1

print(somma/len(lista))


