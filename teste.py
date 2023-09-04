import scipy.io 
import pandas as pd

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/B007.mat")

lista = data['X122_DE_time']

df_b007 = pd.DataFrame(lista, columns=['X_DE'])
df_b007['ROTULO'] = "B007"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/B014.mat")

lista = data['X189_DE_time']

df_b014 = pd.DataFrame(lista, columns=['X_DE'])
df_b014['ROTULO'] = "B014"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/B021.mat")

lista = data['X226_DE_time']

df_b021 = pd.DataFrame(lista, columns=['X_DE'])
df_b021['ROTULO'] = "B021"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/IR007.mat")

lista = data['X109_DE_time']

lista = lista

df_ir007 = pd.DataFrame(lista, columns=['X_DE'])
df_ir007['ROTULO'] = "IR007"


data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/IR014.mat")

lista = data['X173_DE_time']

df_ir014 = pd.DataFrame(lista, columns=['X_DE'])
df_ir014['ROTULO'] = "IR014"


data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/IR021.mat")

lista = data['X213_DE_time']

df_ir021 = pd.DataFrame(lista, columns=['X_DE'])
df_ir021['ROTULO'] = "IR021"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/Normal1797.mat")

lista = data['X097_DE_time']

df_normal1797 = pd.DataFrame(lista, columns=['X_DE'])
df_normal1797['ROTULO'] = "NORMAL1797"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/OR007.mat")

lista = data['X135_DE_time']

df_or007 = pd.DataFrame(lista, columns=['X_DE'])
df_or007['ROTULO'] = "OR007"

data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/OR014.mat")

lista = data['X201_DE_time']

df_or014 = pd.DataFrame(lista, columns=['X_DE'])
df_or014['ROTULO'] = "OR014"


data = scipy.io.loadmat("C:/Users/Cliente/Desktop/data/CWRU/OR021.mat")

lista = data['X238_DE_time']

df_or021 = pd.DataFrame(lista, columns=['X_DE'])
df_or021['ROTULO'] = "OR021"



dataframe = pd.concat([df_b007, df_b014, df_b021, df_ir007, df_ir014,df_ir021,df_normal1797,df_or007, df_or014, df_or021
                       ], ignore_index=False)
dataframe.replace()
print(dataframe.head())

dataframe.to_csv("dados_combinados_completos_DE.csv")