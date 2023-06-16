import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

class persona:
 # nel costruttore andiamo a inizializzare le proprietà
 def __init__(self, nome, anni, stipendio):
  self.nome = nome
  self.anni = anni
  self.stipendio = stipendio

# metodo speciale str che restituisce una stringa con le proprietà
 def __str__(self):
  return f"nome: {self.nome},anni: {self.anni},stipendio:{self.stipendio}"

@app.route('/')
def home():

    p1 = persona("Carlo", 38, 1500)
    p2 = persona("Antonio", 22, 2000)
    p3 = persona("Maria", 25, 2000)
    print(p3.anni)
    print("La somma è", (p1.stipendio+ p2.stipendio + p3.stipendio))
    listaOggetti = list()

    somma = 0
    for i in listaOggetti:
     somma+= i.stipendio

    for nome in listaOggetti:
     print(nome.nome)

    print(somma)

    scelta = "1"

    while scelta!= "0":
     scelta = input("Scegli: ")
     if scelta == "1":
      listaOggetti.append(p1)
     elif scelta == "2":
      listaOggetti.append(p2)
     elif scelta == "3":
      listaOggetti.append(p3)
    total_stipendio = 0  # Totale degli stipendi
    labels = []
    values = []
    for i in listaOggetti:
        if i.nome not in labels:  # Verifica se l'etichetta è già presente nella lista
            labels.append(i.nome)
            values.append(1)
        else:
            index = labels.index(i.nome)  # Ottieni l'indice dell'etichetta già presente
            values[index] += 1  # Incrementa il valore corrispondente all'etichetta
        total_stipendio += i.stipendio

        # Calcola il dipendente più e meno presenti
    max_presence = max(values)
    min_presence = min(values)
    max_employee = labels[values.index(max_presence)] # assegna a maxemployee il dipendente con l'eticchetta con le massime presente
    min_employee = labels[values.index(min_presence)]
    print(max_employee)
    max_pr = []
    min_pr = []
    for j in labels:
        if labels[values.index(max_presence)] == j[values.index(max_presence)]:
         print(j)


    print(max_pr)







    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Distribuzione dipendenti")

    # Salva il grafico come immagine
    image_path = 'static/pie_chart.png'
    plt.savefig(image_path)

    return render_template('index.html', image_path=image_path, total_stipendio=total_stipendio,max_pr=max_pr, min_pr=min_pr)

if __name__ == '__main__':
    app.run()