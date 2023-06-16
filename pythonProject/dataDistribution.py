import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio
data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])

# Calcola la distribuzione dei dati
unique_values, counts = np.unique(data, return_counts=True)
data_distribution = dict(zip(unique_values, counts))

# Crea il grafico
plt.bar(data_distribution.keys(), data_distribution.values())
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.title('Data Distribution')
plt.show()
