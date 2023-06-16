import matplotlib.pyplot as plt

# Dati di esempio
labels = ['Rosso', 'Verde', 'Blu', 'Giallo']
sizes = [30, 20, 15, 35]
colors = ['red', 'green', 'blue', 'yellow']

# Crea un grafico a torta
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Aggiungi un titolo al grafico
plt.title("Grafico a torta")

# Mostra il grafico
plt.show()
