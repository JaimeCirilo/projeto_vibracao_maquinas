import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("C:/Users/Cliente/Desktop/data/dados_FE.csv")
lista_rotulos =["B007", "B014", "B021", "IR007", "IR014", "IR021", "NORMAL1797","OR007", "OR014", "OR021"]

index = 1
for rotulo in lista_rotulos:
    filtro = dataframe["ROTULO"] == rotulo
    df_filtro = dataframe[filtro]
    plt.subplot(2,5, index)
    plt.title(rotulo)
    plt.plot(df_filtro["X_FE"])
    index+=1

plt.suptitle("X FE")
plt.show()