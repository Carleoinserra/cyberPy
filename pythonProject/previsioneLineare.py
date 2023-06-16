import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Dati di esempio
date = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # Sequenza temporale (giorni)
values = np.array([10, 12, 15, 18, 20, 22, 24, 25])  # Valori associati alla sequenza temporale

# Reshape dei dati per la regressione lineare
X = date.reshape(-1, 1)
y = values

# Crea un modello di regressione lineare
model = LinearRegression()
model.fit(X, y)

# Genera una sequenza temporale futura per la previsione
future_dates = np.arange(9, 13).reshape(-1, 1)

# Effettua la previsione sui dati futuri
predicted_values = model.predict(future_dates)

# Plot dei dati originali e della previsione
plt.scatter(date, values, color='blue', label='Dati originali')
plt.plot(date, model.predict(X), color='red', label='Linea di regressione')
plt.plot(future_dates, predicted_values, color='green', label='Previsione')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.title('Previsione dei dati futuri')
plt.legend()

# Mostra il grafico
plt.show()
