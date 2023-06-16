from flask import Flask, redirect, url_for, request, render_template
from Auto import Auto
from flask_mail import Mail, Message
import mysql.connector
import random
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
Cassa = []


listaAuto =[]

@app.route('/')
def hello_name():
    return render_template('home.html')

@app.route('/listaCar')
def listaCar():
    return render_template('listaAuto.html')

@app.route('/success/')
def success():

    return render_template('result.html', nome = listaAuto)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        cont = random.randint(1, 10000)

        stringa = request.form['pm'].split(",")
        colore = request.form['rm']
        email = request.form['xm']
        auto = Auto(stringa[0], colore, stringa[1], email, cont)
        print(auto)
        listaAuto.append(auto)

        return redirect(url_for('success'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success'))

@app.route('/send',methods=['POST', 'GET'])
def send():


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE testAuto")
    mycursor.close()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test",
        database="testAuto"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, marca VARCHAR(255), colore VARCHAR(255)), prezzo VARCHAR(255), email VARCHAR(255), num VARCHAR(255)")
    for x in listaAuto:
         sql = "INSERT INTO customers (marca, colore, prezzo, email,num) VALUES (%s, %s,%s,%s,%s)"
         val = (x.marca, x.colore,x.prezzo,x.email, str(x.num))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



    for x in listaAuto:

      adresse = x.email
      msg = Message('Hello', sender='fullstackinserra@gmail.com', recipients=[adresse])
      prezzo = x.prezzo
      msg.body = "Buongiono messaggio mandato dalla concessionaria" \
                 " il prezzo dell'auto " + x.marca + " selezionata è "+ prezzo + " euro"
      mail.send(msg)
      numpre = int(prezzo)
      cassa.append(numpre)
      print(x)


    listaAuto.clear()
    return redirect(url_for('conto'))
if __name__ == '__main__':
    app.run(debug=True)