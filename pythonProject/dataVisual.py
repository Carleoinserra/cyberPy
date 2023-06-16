import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Crea un grafico a dispersione
plt.scatter(x, y)

# Aggiungi etichette agli assi
plt.xlabel("X")
plt.ylabel("Y")

# Aggiungi un titolo al grafico
plt.title("Grafico a dispersione")

# Mostra il grafico
plt.show()
