from flask import Flask, redirect, url_for, request, render_template
from Auto import Auto
from flask_mail import Mail, Message
from pymongo import MongoClient
import pymongo
import random
app = Flask(__name__)
mail=Mail(app)

# creiamo e connettiamoci al database




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

@app.route('/check',methods=['POST', 'GET'])
def check():
 if request.method == 'POST':
  myclient = pymongo.MongoClient('mongodb://localhost:27017/')
  mydb = myclient['testAuto']
  mycol = mydb["interessi"]
  numid =[]
  selected = []
  cont = 0
  '''for x in mycol.find({}, {"_id": 0 ,"marca": 0, "colore": 0, "Prezzo": 0, "Email": 0}):
      cont += 1
      num = str(x["Num"])'''

  selected = request.form.getlist("pm")
  for x in selected:

   myquery = {'num': x}
   print(myquery)
   print(mycol.delete_one(myquery))
   print (x)






 """ for x in mycol.find({}, {"marca": 0, "colore": 0, "Prezzo": 0, "Email": 0}):
     print(str(x["_id"]))"""


 return render_template('result.html', nome = listaAuto)

@app.route('/admin',methods=['POST', 'GET'])
def admin():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['testAuto']
    mycol = mydb["interessi"]
    cont = 0
    for x in mycol.find({}, {"marca": 0, "colore": 0, "Prezzo": 0, "Email": 0}):
        cont += 1
        numid = str(x["_id"])
    return render_template('amministratore1.html', lista = mycol)


@app.route('/send',methods=['POST', 'GET'])
def send():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['testAuto']
    mycol = mydb["interessi"]
    '''for x in mycol.find({}, {"marca": 0, "colore": 0, "Prezzo": 0, "Email": 0}):
        print(x["Num"])'''





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
      mydict = {"marca": x.marca, "colore": x.colore, "Prezzo": x.prezzo, "Email": x.email, "num": x.num}

      mycol.insert_one(mydict)

    listaAuto.clear()
    return redirect(url_for('conto'))

@app.route('/conto/', methods=['POST', 'GET'])
def conto():
    somma = 0
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["testAuto"]
    mycol = mydb["interessi"]

    for x in mycol.find({}, {"_id": 0, "marca": 0, "colore": 0, "Email": 0}):
     print (x["Prezzo"])
     tot = int(x["Prezzo"])
     somma += tot




    return render_template('arrivederci.html')






@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        cont = random.randint(1, 10000)
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['testAuto']
        mycol = mydb["interessi"]
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


if __name__ == '__main__':
    app.run(debug=True)
