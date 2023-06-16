def verifica_credenziali(username, password):


    # Dati di accesso corretti
    username_corretto = "esempio_username"
    password_corretta = "esempio_password"

    if username == username_corretto and password == password_corretta:
        print("Login effettuato.")
    elif username != username_corretto and password != password_corretta:
        print("Username e password non corretti.")
    elif username != username_corretto:
        print("Username non corretto.")
    else:
        print("Password non corretta.")

# Test del programma
input_username = input("Inserisci il nome utente: ")
input_password = input("Inserisci la password: ")

verifica_credenziali(input_username, input_password)
