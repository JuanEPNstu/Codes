import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)       # Rango de valores de x
y = np.exp(1-x**2)                  # Función 

nombre_f = "Exponencial"
plt.plot(x, y, label='y')
plt.title(f"Función {nombre_f}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
