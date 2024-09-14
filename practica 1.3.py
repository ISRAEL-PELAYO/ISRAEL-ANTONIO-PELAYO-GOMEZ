import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulamos un dataset de correos electrónicos con las siguientes características:
# - longitud del asunto
# - cantidad de enlaces en el correo
# - etiqueta de clasificación: 'spam' o 'no spam'
data = {'Asunto_Longitud': [5, 50, 60, 10, 3, 45, 70, 4, 15, 35],
        'Enlaces': [0, 10, 15, 1, 0, 12, 14, 1, 2, 5],
        'Etiqueta': ['no spam', 'spam', 'spam', 'no spam', 'no spam', 'spam', 'spam', 'no spam', 'no spam', 'spam']}

# Convertimos el dataset en un DataFrame
df = pd.DataFrame(data)

# Imprimir el encabezado del DataFrame
print(df.head())

# Extrae las características (X) y etiquetas (y)
y = df['Etiqueta'].values
y = np.where(y == 'spam', 1, -1)  # Spam = 1, No spam = -1
X = df[['Asunto_Longitud', 'Enlaces']].values

# Visualiza los datos antes de entrenar el perceptron
plt.scatter(X[y == -1, 0], X[y == -1, 1], color='red', marker='o', label='no spam')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', marker='x', label='spam')
plt.xlabel('Longitud del Asunto')
plt.ylabel('Cantidad de Enlaces')
plt.legend(loc='upper left')
plt.show()

# Implementacion del algoritmo de Perceptron
class Perceptron:
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calcular la entrada neta."""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Devolver la clase predicha."""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Entrenamos el perceptron con los datos de correos electronicos
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

# Grafica el numero de errores durante cada epoca
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Épocas')
plt.ylabel('Número de errores')
plt.title('Errores durante el entrenamiento (Spam vs No Spam)')
plt.show()

# Visualizacion de las regiones de decision
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

# Mostrar las regiones de decision
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('Longitud del Asunto')
plt.ylabel('Cantidad de Enlaces')
plt.legend(loc='upper left')
plt.title('Regiones de decisión (Spam vs No Spam)')
plt.show()
