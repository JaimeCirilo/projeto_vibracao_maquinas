import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import os
import scipy.io

file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/IR007.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/B007.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/OR007.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/IR014.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/B014.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/OR014.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/IR021.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/B021.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/OR021.mat'
file_path = 'C:/Users/Eggleston/Desktop/CWRU 48K/Normal1797.mat'

# Carregar dados do arquivo .mat usando scipy.io.loadmat
dataIR007 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/IR007.mat')
dataB007 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/B007.mat')
dataOR007 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/OR007.mat')
dataIR014 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/IR014.mat')
dataB014 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/B014.mat')
dataOR014 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/OR014.mat')
dataIR021 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/IR021.mat')
dataB021 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/B021.mat')
dataOR021 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/OR021.mat')
data1797 = scipy.io.loadmat('C:/Users/Eggleston/Desktop/CWRU 48K/Normal1797.mat')

mdataIR007 = dataIR007.keys()
mdataB007 = dataB007.keys()
mdataOR007 = dataOR007.keys()
mdataIR014 = dataIR014.keys()
mdataB014 = dataB014.keys()
mdataOR014 = dataOR014.keys()
mdataIR021 = dataIR021.keys()
mdataB021 = dataB021.keys()
mdataOR021 = dataOR021.keys()
mdata1797 = data1797.keys()

print(mdataIR007)
print(mdataB007)
print(mdataOR007)
print(mdataIR014)
print(mdataB014)
print(mdataOR014)
print(mdataIR021)
print(mdataB021)
print(mdataOR021)
print(mdata1797)

# Imprimir todas as chaves disponíveis
print(dataIR007.keys())
print(dataB007.keys())
print(dataOR007.keys())
print(dataIR014.keys())
print(dataB014.keys())
print(dataOR014.keys())
print(dataIR021.keys())
print(dataB021.keys())
print(dataOR021.keys())
print(data1797.keys())

# matriz que você deseja plotar
image_data = dataIR007['X109_DE_time']
dataIR007
image_data = dataB007['X122_DE_time']
dataB007
image_data = dataOR007['X135_DE_time']
dataOR007
image_data = dataIR014['X173_DE_time']
dataIR014
image_data = dataB014['X189_DE_time']
dataB014
image_data = dataOR014['X201_DE_time']
dataOR014
image_data = dataIR021['X213_DE_time']
dataIR021
image_data = dataB021['X226_DE_time']
dataB021
image_data = dataOR021['X238_DE_time']
dataOR021
image_data = data1797['X097_DE_time']
data1797

# Dados CWRU 48 - IR007 - B007 - OR007
#--------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X109_DE_time'
matriz = np.array(dataIR007['X109_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#---------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X122_DE_time'
matriz = np.array(dataB007['X122_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#----------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X135_DE_time'
matriz = np.array(dataOR007['X135_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

# Dados CWRU 48 - IR014 - B014 - OR014
#-----------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X173_DE_time'
matriz = np.array(dataIR014['X173_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#--------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X189_DE_time'
matriz = np.array(dataB014['X189_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#--------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X201_DE_time'
matriz = np.array(dataOR014['X201_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#---------------------------------------------------------------------------
# Dados CWRU 48 - IR021 - B021 - OR021
#--------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X213_DE_time'
matriz = np.array(dataIR021['X213_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#--------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X226_DE_time'
matriz = np.array(dataB021['X226_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#-------------------------------------------------------------------------
# Criar uma matriz a partir dos valores associados à chave 'X238_DE_time'
matriz = np.array(dataOR021['X238_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()

#----------------------------------------------------------------------------
# Dados CWRU 48 - NORMAL1797
# Criar uma matriz a partir dos valores associados à chave 'X097_DE_time'
matriz = np.array(data1797['X097_DE_time'])
print(matriz)
plt.plot(matriz)
matriz.shape

# Tamanho desejado para cada parte
tamanho_parte = len(matriz) // 1000  # Dividir o comprimento total pela quantidade de partes desejada

# Dividir a matriz em partes de tamanho igual
partes = [matriz[i:i + tamanho_parte] for i in range(0, len(matriz), tamanho_parte)]

# Verificar o número de partes criadas
print(len(partes))

# Plotar a primeira parte para verificar
plt.plot(partes[0])
plt.show()














