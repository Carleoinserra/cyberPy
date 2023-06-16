import requests

def scan_website_security(url):
    try:
        # Avvia il proxy ZAP
        proxy = {
            'http': 'http://localhost:8080',
            'https': 'http://localhost:8080'
        }

        # Configura il proxy per le richieste
        session = requests.Session()
        session.proxies = proxy

        # Accedi all'URL target
        response = session.get(url)

        # Genera un report di sicurezza utilizzando ZAP
        zap_api_url = "http://localhost:8080/JSON/ascan/action/scan/?url=" + url
        response = session.get(zap_api_url)

        print("Scansione avviata. Controlla l'interfaccia di OWASP ZAP per il report completo.")

    except requests.exceptions.RequestException as e:
        print("Si è verificato un errore durante la connessione al sito web:", str(e))

# Esempio di utilizzo
website_url = "https://www.google.com"
scan_website_security(website_url)
