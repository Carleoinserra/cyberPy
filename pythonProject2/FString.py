#f"Nome: {cognome} Anni: {self.anni} Stipendio: {self.stipendio}    "

# Le stringhe formattate, chiamate anche f-string, hanno il prefisso
# f o F e consentono di inserire delle espressioni Python nella stringa,
# racchiudendole dentro parentesi graffe.
import OggettoSemplice
print  (f"il valore di c1 {OggettoSemplice.c1.x}")


OggettoSemplice.c1.x = 7
f = open("Oggetto.", "w")
f.write(str(OggettoSemplice.c1.x))
f.close()
f = open("file", "r")
y = int(f.readline())
print(y)
