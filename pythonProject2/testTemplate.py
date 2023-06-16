from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_name():
   return render_template('form.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      nome = request.form['nm']

      return redirect(url_for('success',name = nome))
   else:
      nome = request.args.get('nm')
      return redirect(url_for('success',name = nome))

@app.route('/success/<name>')
def success(name):
    return render_template('stampaNome.html', nome=name)

if __name__ == '__main__':
   app.run(debug = True)
