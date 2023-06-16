from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    invia_email()
    return render_template('index.html')

@app.route('/invia_email')
def invia_email():
    # Impostazioni dell'email
    sender_email = "inserracarlo@gmail.com"
    sender_password = "zpomjjbfcodkzxro"
    recipient_email = "inserracarlo@gmail.com"
    subject = "Collegamento ad una pagina HTML"

    # Generazione del collegamento alla pagina HTML
    collegamento_html = "http://localhost:5000/pagina_login"

    # Creazione del corpo dell'email
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    html_content = f"""
    <html>
    <body>
        <h2>Collegamento ad una pagina HTML</h2>
        <p>Clicca sul seguente collegamento per accedere alla pagina:</p>
        <a href="{collegamento_html}">Accedi</a>
    </body>
    </html>
    """

    part = MIMEText(html_content, "html")
    message.attach(part)

    # Invio dell'email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email inviata correttamente!")
    except Exception as e:
        print("Si è verificato un errore durante l'invio dell'email:", str(e))

    return "L'email è stata inviata correttamente!"


@app.route('/pagina_login', methods=['GET', 'POST'])
def pagina_login():
  if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print("Username:", username)
        print("Password:", password)



        return "Autenticazione effettuata con successo!"

  return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
