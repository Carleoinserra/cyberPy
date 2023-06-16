"""
In python gli oggetti sono detti classi la sintassi per la definizione è simile alle function
"""

class oggetto:
    x = 5

c1 = oggetto()

print(c1.x)
""" 
Quando creiamo un oggettodi solito è molto utile inserire un costruttore
un costruttore possiede delle variabili che vengono istanziate nel momento della creazione dell'oggetto
per fare questo python utilizza una funzione chiamata _init_()
sostanzialmente una funzione che inizializza l'oggetto, di solito con valori inserite come
parametri


"""
class Dipendente:
    def __init__(self, cognome, anni, stipendio):
        self.cognome = cognome
        self.anni = anni
        self.stipendio = stipendio

    def __str__(self):
        return f"Nome: {self.cognome} Anni: {self.anni} Stipendio: {self.stipendio}    "

    def bonus(self, x):
       self.stipendio += x

d1 = Dipendente("Bianchi", 36, 2000)

print(d1.cognome + " " , d1.stipendio)
print(d1)
d1.bonus(200)
print(d1.cognome + " " , d1.stipendio)

listaDipendenti =[]
listaDipendenti.append(d1)

print(listaDipendenti[0])
"""
con la funzione _str_ andiamo a definire la visualizzazione dell'oggetto
possiamo definire anche funzioni semplici per le classi
FUNZIONE DI SELF
Il parametro self è un riferimento all'istanza corrente della classe e viene utilizato
per accedere alle variabili che appartengono alla classe

Non deve essere chiamato self, puoi chiamarlo come preferisci, ma deve essere il primo parametro
di qualsiasi funzione nella class

"""