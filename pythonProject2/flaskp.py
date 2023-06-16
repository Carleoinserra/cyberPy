# Importazione della classe Flask
from flask import Flask
import OggettoSemplice
# Creazione dell'oggetto Flask
app = Flask(__name__)

x = OggettoSemplice.c1.x
print(x)

@app.route("/")
@app.route("/home")
def home():
   return f"il valore di c1 {OggettoSemplice.c1.x}"

if __name__ == "__main__":
    app.run()



