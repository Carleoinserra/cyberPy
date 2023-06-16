from flask import Flask, redirect, url_for, request, render_template
from Auto import Auto
from flask_mail import Mail, Message
app = Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fullstackinserra@gmail.com'
app.config['MAIL_PASSWORD'] = 'azaihbytorsokrxn'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

help('print')
@app.route('/')
def hello_name():
    return render_template('scegliAuto.html')


@app.route('/success')
def success(name):
    nome = name
    return render_template('result.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        MarcaAuto = request.form.items('pm')

        

        return redirect(url_for('success'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success'))
@app.route('/send')
def send():

    msg = Message('Hello', sender='fullstackinserra@gmail.com', recipients=['inserracarlo@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)

