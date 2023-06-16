from Persona import Persona


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self,nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie Insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda
    def __repr__(self):
            return "insegnante"

#d1 = Insegnante("Aldo", "Bianchi", 45, "Via Milano 4", ["Italiano", "Storia"])
#print(d1.scheda_personale())

