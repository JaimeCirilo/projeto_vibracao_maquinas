import scipy.io 
import pandas as pd

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/normal.mat")

keys = data.keys()

print(keys)

lista = data['X097_DE_time']
lista2 = data['X097_FE_time']

lista_de_tuplas = list(zip(lista,lista2))

df = pd.DataFrame(lista_de_tuplas, columns=['X_DE',"X_FE"])
df['ESTADO'] = "NORMAL"

print(df.head())


lista2 = data['X238_FE_time']
lista2 = data['X201_FE_time']
lista2 = data['X135_FE_time']
lista2 = data['X097_FE_time']
lista2 = data['X213_FE_time']
lista2 = data['X173_FE_time']
lista2 = data['X109_FE_time']
lista2 = data['X226_FE_time']
lista2 = data['X189_FE_time']
lista2 = data['X122_FE_time']
