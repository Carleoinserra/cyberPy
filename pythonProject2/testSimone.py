from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# Displaying MENU
@app.route("/")
def myResturant():
    return render_template('Flask5.html')

# Displaying PRICE
@app.route('/success/<name>')
def success(name):
   menu = name
   return render_template('Flask6.html', nome = menu)

# Printing PRICE
@app.route('/form',methods = ['POST', 'GET'])
def form():
   if request.method == 'POST':
      menu = request.form['mn']
      print(menu)
      return redirect(url_for('success', name = menu))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)