from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('login.html')

@app.route('/success/<name>/<surname>')
def success(name, surname):
   print(name)
   print(surname)
   return render_template('stampaNomi.html', nome = name ,cognome = surname)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      nome = request.form['nm']
      cognome = request.form['pm']
      return redirect(url_for('success',name = nome, surname = cognome))
   else:
      nome = request.form['nm']
      cognome = request.form['pm']

      return redirect(url_for('success',name = nome, surname = cognome))

if __name__ == '__main__':
   app.run(debug = True)