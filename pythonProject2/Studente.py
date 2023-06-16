from Persona import Persona


class Studente(Persona):
    profilo = "Studente"

    def __init__(self,nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda
    def __repr__(self):
            return "studente"

#s1 = Studente("Mario", "Rossi", 28, "Via Roma", "Fisica")
#rint(s1.scheda_personale())
