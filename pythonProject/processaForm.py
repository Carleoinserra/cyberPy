from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np
import Oggetto

app = Flask(__name__)
persone = []
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
     user = request.form.get('nm')
     stipendio = 0
     if user == "Carlo":

         p = Oggetto.persona("Carlo",35, 1000)
     if user == "Antonio":
         p = Oggetto.persona("Antonio",36, 1100)
     if user == "Maria":
         p = Oggetto.persona("Maria", 37, 1200)
     persone.append(p)
     return redirect(url_for('success',name = user))
  else:
     user = request.form.get('nm')
     return redirect(url_for('success',name = user))

@app.route('/gestore',methods = ['POST', 'GET'])
def gestore():
    categories = {}
    for persona in persone:
        nome = persona.nome
        if nome in categories:
            categories[nome] += 1
        else:
            categories[nome] = 1


    # Prepara i dati per il grafico a torta
    labels = list(categories.keys())
    values = list(categories.values())

    # Genera il grafico a torta
    plt.figure(figsize=(6, 6))
    plt.subplot(211)
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # Assicura un aspetto circolare al grafico

    # Prepara i dati per l'istogramma
    labels_istogramma = list(categories.keys())
    values_istogramma = list(categories.values())

    # Genera l'istogramma
    plt.subplot(212)
    plt.bar(labels_istogramma, values_istogramma)
    plt.xlabel('Nome')
    plt.ylabel('Conteggio')
    plt.title('Istogramma')



    # Calcola la retta di regressione lineare
    x = np.arange(len(values_istogramma))
    y = np.array(values_istogramma)
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * x + intercept



    # Aggiungi la previsione lineare al grafico a torta e all'istogramma
    plt.subplot(211)
    plt.plot(x, regression_line, color='red', label='Previsione lineare')

    plt.legend()

    plt.subplot(212)
    plt.plot(x, regression_line, color='red', label='Previsione lineare')

    plt.legend()



    # Salva il grafico come immagine
    graph_path = 'static/graph.png'  # Percorso dell'immagine di output
    plt.savefig(graph_path)
    return render_template("gestore.html", graph_path=graph_path, persone = persone)

@app.route('/success/<name>')
def success(name):
  return 'welcome %s' % name

if __name__ == '__main__':
    app.run()