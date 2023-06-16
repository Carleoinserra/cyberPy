class Auto:
    def __init__(self, marca, colore, prezzo, email, num):
        self.marca = marca
        self.colore = colore
        self.prezzo = prezzo
        self.email = email
        self.num = num
    def __str__(self):
        return f"Marca: {self.marca}, Colore: {self.colore}, Prezzo: {self.prezzo}, Email: {self.email} Num: {self.num}"

listaAuto = []

'''
class AutoSalone:

  def aggiungiAuto(self,marca, modello, anno):

      listaAuto.append(Auto(marca,modello,anno))

  def visualizza(self):

      for x in listaAuto:

          print(x)







a1 = AutoSalone()

a1.aggiungiAuto("Renault", "Clio","2007")
(a1.visualizza())

'''