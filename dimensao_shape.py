import numpy as np

# URL para o arquivo CSV
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'

# Carrega os dados do CSV para um array NumPy
dado = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)

# Verifica as dimensões do array 'dado'
print(dado.shape)

# Outra forma de verificar as dimensões usando np.shape()
print(np.shape(dado))
