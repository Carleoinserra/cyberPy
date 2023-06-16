from flask import Flask, redirect, url_for, request, render_template
from NomiUser import listaNomi
app = Flask(__name__)
nome = ""
cognome = ""

@app.route('/')
def hello_name():
   return render_template('scegliAuto.html')

@app.route('/success/<name>')
def success(name):
   nome = name
   return render_template('result.html', name = nome)


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':

      prezzo1 = request.form['pm']
      prezzo2 = request.form['xm']
      prezzo3 = request.form['tm']
      prezzo = int(prezzo1) + int(prezzo2) + int(prezzo3)

      



      return redirect(url_for('success', name = prezzo))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)