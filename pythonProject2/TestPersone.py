
from Studente import Studente
from Insegnante import Insegnante

listaPersone = []
d1 = Insegnante("Aldo", "Bianchi", 45, "Via Milano 4", ["Italiano", "Storia"])
s1 = Studente("Mario", "Rossi", 28, "Via Roma", "Fisica")
listaPersone.append(d1)
listaPersone.append(s1)

for x in listaPersone:


      print(x.corso_di_studio)

