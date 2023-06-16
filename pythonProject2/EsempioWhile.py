# in questo programma iteriamo una istruzione con while stabilendo una condizione

parola = input("scrivi una parola")
cont = 0
while parola != "0":
    print(parola)
    cont += 1
    parola = input("scrivi una parola")

print("Si contano", cont, "iterazioni")

lista = [1,2,3,4]

lista1 = []

lista1.append("3")

lista1.insert(0, 4)

