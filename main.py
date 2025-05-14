import numpy as np
import matplotlib.pyplot as plt

# Intervalo de x
x = np.linspace(-10, 10, 400)

# Funções
funcoes = [
    (x, x, 'Linear (x)'),
    (x, x**2, 'Parábola (x²)'),
    (x, x**3, 'Cúbica (x³)'),
    (x, x**4, 'Quartica (x⁴)'),
    (x, np.sin(x), 'Seno (sin(x))'),
    (x, np.cos(x), 'Cosseno (cos(x))'),
    (x, np.exp(-x**2), 'Gaussiana (e^(-x²))'),
    (x, 1 / (1 + np.exp(-x)), 'Sigmoide (1 / (1 + e^(-x)))')
]

# Criar subgráficos 4x2
fig, axes = plt.subplots(4, 2, figsize=(12, 10))
axes = axes.flatten()

# Plotar cada função
for i, (x_vals, y_vals, titulo) in enumerate(funcoes):
    axes[i].plot(x_vals, y_vals)
    axes[i].set_title(titulo)
    axes[i].grid(True)
    axes[i].axhline(0, color='black', linewidth=0.5)
    axes[i].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
