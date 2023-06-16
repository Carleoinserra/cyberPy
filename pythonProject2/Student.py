class Student:

    def __init__(self, nome, cognome, anni, matricola):
        self.nome = nome
        self.cognome = cognome
        self.anni = anni
        self.matricola = matricola
        self.lista = []

    def __str__(self):
        return self.nome + " " + self.cognome + " " + self.anni + " " + self.matricola

    def inserisciVoto(self, voto):
        self.lista.append(voto)

    def mediavoto(self):
        somma = 0
        cont = 0
        for x in self.lista:
            cont += 1
            somma += x

        print(somma / cont)

student1 = Student("Antonio", "Rossi", "29", "1234")

print(student1)

student1.inserisciVoto(25)
student1.inserisciVoto(26)
student1.inserisciVoto(27)

student1.mediavoto()