from flask import Flask, redirect, url_for, request, render_template
from NomiUser import listaNomi
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    for x in listaNomi:
     print (x)
     p  = ' '.join(listaNomi)

    return p

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      listaNomi.append(user)
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)