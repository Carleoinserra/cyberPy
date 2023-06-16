from flask import Flask, redirect, url_for, request, render_template
from NomiUser import listaNomi
app = Flask(__name__)
nome = ""
cognome = ""

@app.route('/')
def hello_name():
   return render_template('menu.html')

@app.route('/success/<name>')
def success(name):
   nome = name
   return render_template('result.html', name = nome)


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      nome = request.form['nm']
      cognome = request.form['pm']

      if nome == "Antonio" and cognome == "Rossi":
       user = "login corretto" + nome + " " + cognome
      else:
       user = "login non corretto"

      return redirect(url_for('success', name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)