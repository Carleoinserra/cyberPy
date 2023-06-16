import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Dati del mittente
sender_email = "inserracarlo@gmail.com"
sender_password = "xobxkbzbbwouycom"

# Dati del destinatario
recipient_email = "inserracarlo@gmail.com"

# Creazione del messaggio
message = MIMEMultipart("alternative")
message["Subject"] = "Collegamento ad una pagina HTML"
message["From"] = sender_email
message["To"] = recipient_email

# Testo del messaggio in formato HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>Accesso protetto</title>
</head>
<body>
  <h1>Accesso protetto</h1>
  
  <form action="processa_login.py" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required><br><br>
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required><br><br>
    
    <input type="submit" value="Accedi">
  </form>
</body>
</html>

"""

# Aggiunta del testo HTML al messaggio
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
