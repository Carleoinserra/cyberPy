class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")

    def __repr__(self):
            return "persona"

class Studente(Persona):
    pass

class Insegnante(Persona):
    pass


studente_uno = Studente("Py", "Mike", 24, "Casa Dello Studente")
insegnante_uno = Insegnante("Mario", "Rossi", 33, "Viale Roma 32")

#print(studente_uno.scheda_personale())
#print(insegnante_uno.scheda_personale())

