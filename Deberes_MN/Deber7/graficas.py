import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1000)       # Rango de valores de x
y = np.exp(-x**3)-np.cos(x)                  # Función 

nombre_f = "del ejercicio"
plt.plot(x, y, label='y')
plt.title(f"Función {nombre_f}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
