import pickle
class oggetto:
   x = 5

   def __str__(self):
    return f"Oggetto semplice con valore: {self.x} "



c1 = oggetto()
c2 = oggetto()
c2.x = 6
lista = []
lista.append(c1)
lista.append(c2)
# apriamo un strem di scrittura: attenzioni siccome vogliamo salvare oggetti e non stringhe
# salviamo i dati in un file binario di non testOggetto e scriviamo con una sintassi diversa non più "w" write
# ma write binary

f = open("testEs.pkl", "wb")

pickle.dump(lista, f)

f.close()

f = open("testEs.pkl", "rb")
unpickler = pickle.Unpickler(f);
listaDaLettura = unpickler.load();
f.close()
for i in listaDaLettura:
            print(i)

f.close()
