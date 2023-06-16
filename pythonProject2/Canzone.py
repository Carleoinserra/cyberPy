class Canzone:
    def __init__(self, titolo, anno, autore):
        self.titolo = titolo
        self.anno = anno
        self.autore = autore

    def __str__(self):
        return f"Nome: {self.titolo} Anno: {self.anno} Autore: {self.autore}    "

    def bonus(self, x):
       self.stipendio += x

d1 = Canzone("Bianchi", 2000, "Conte")

lista = []
lista.append(d1)

for i in lista:
    print (i)