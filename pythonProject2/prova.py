from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route("/")
def hello():

 return  render_template('menu.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
  print("ciao")
  if request.method == 'POST':
    name = request.form['nm']
    return redirect(url_for('success',name= name))
  else:
    name = request.args.get('nm')
    return redirect(url_for('success',name = name))

@app.route('/success/<name>')
def success(name):
    return render_template('result.html', name=name)

if __name__ == '__main__':
 app.run()
