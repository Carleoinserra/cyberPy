from flask import Flask, redirect, url_for, request, render_template
from Auto import Auto
from flask_mail import Mail, Message
app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fullstackinserra@gmail.com'
app.config['MAIL_PASSWORD'] = 'azaihbytorsokrxn'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
cassa = []

listaAuto =[]

@app.route('/')
def hello_name():
    return render_template('ListaAuto.html')


@app.route('/success/')
def success():

    return render_template('result.html', nome = listaAuto)


@app.route('/send',methods=['POST', 'GET'])
def send():
    cont = 0
    for x in listaAuto:

      adresse = x.email
      msg = Message('Hello', sender='fullstackinserra@gmail.com', recipients=[adresse])
      prezzo = x.prezzo
      msg.body = "Buongiono messaggio mandato dalla concessionaria" \
                 " il prezzo dell'auto " + x.marca + " selezionata è "+ prezzo + " euro"
      mail.send(msg)
      numpre = int(prezzo)
      cassa.append(numpre)


    listaAuto.clear()
    return redirect(url_for('conto'))

@app.route('/conto/', methods=['POST', 'GET'])
def conto():
    somma = 0
    for x in cassa:
      somma += x

    return render_template('incasso.html', incasso=somma)






@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        stringa = request.form['pm'].split(",")
        colore = request.form['rm']
        email = request.form['xm']
        auto = Auto(stringa[0], colore, stringa[1], email)
        print(auto)
        listaAuto.append(auto)

        return redirect(url_for('success'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success'))


if __name__ == '__main__':
    app.run(debug=True)
    print  (help())