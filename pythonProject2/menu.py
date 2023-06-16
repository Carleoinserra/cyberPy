from flask import Flask, redirect, url_for, request, render_template

from flask_mail import Mail, Message

from OggettoMenu import Menu


app = Flask(__name__)
cassa = 0
listaMenu = []

@app.route("/")
def hello():
    return render_template('test.html')


@app.route('success/<mail>/')
def success(mail):
    return render_template("score.html", mail = mail)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        first = request.form['firstPlate']

        second = request.form['secondPlate']

        third = request.form['thirdPlate']

        price = int(first) + int(second) + int(third)

        mail = request.form['email']

        newMenu = Menu(first, second, third, price, mail)
        listaMenu.append(newMenu)
        for x in listaMenu:
         x.first
        return redirect(url_for('success', mail=mail))

    else:

        first = request.args.get('firstPlate')

        second = request.args.get('secondPlate')

        third = request.args.get('thirdPlate')

        price = int(first) + int(second) + int(third)

        mail = request.arg.get('email')

        newMenu = Menu(first, second, third, price, mail)

        return redirect(url_for('success', mail=mail))


if __name__ == '__main__':
 app.run(debug=True)
