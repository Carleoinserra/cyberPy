lista = []
x = int(input("scrivi un numero: "))
cont = 0
while x != 0:
    lista.insert(cont, x)
    x = int(input("scrivi un numero: "))
    cont +=1

for x in lista:
    print(x)