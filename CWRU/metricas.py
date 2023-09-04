import pandas as pd
import numpy as np

dataframe = pd.read_csv("C:/Users/Cliente/Desktop/data/dados_DE.csv")
dataframe_metricas = pd.DataFrame({"MAX":[],"MIN":[],"MEAN":[],"STD":[],"SKEW":[],"KURTOSIS":[],"CREST":[],"ROTULO":[]})

lista_rotulos =["B007", "B014", "B021", "IR007", "IR014", "IR021", "NORMAL1797","OR007", "OR014", "OR021"]

for rotulo in lista_rotulos:
    inicio = 0
    filtro_rotulo = dataframe["ROTULO"] == rotulo
    df_por_rotulo = dataframe[filtro_rotulo]
    print(rotulo)
    print(df_por_rotulo.head())
    for final in range(inicio,len(df_por_rotulo),1000):
        df_filtro_por_mil = df_por_rotulo[inicio:final]
        max = df_filtro_por_mil["X_DE"].max()
        min = df_filtro_por_mil["X_DE"].min()
        mean = df_filtro_por_mil["X_DE"].mean()
        std= df_filtro_por_mil["X_DE"].std()
        skewness = df_filtro_por_mil["X_DE"].skew(axis=0)
        kurtosis = df_filtro_por_mil["X_DE"].kurtosis(axis=0)
        crest = np.max(np.abs(df_filtro_por_mil["X_DE"]))/np.sqrt(np.mean(np.square(df_filtro_por_mil["X_DE"])))

        linha_df = pd.DataFrame({"MAX":[max],"MIN":[min],"MEAN":[mean],"STD":[std],"SKEW":[skewness],"KURTOSIS":[kurtosis],"CREST":[crest],"ROTULO":[rotulo]})
        dataframe_metricas = pd.concat([dataframe_metricas,linha_df])
        inicio = final
dataframe_metricas.replace("","NaN")
dataframe_metricas.dropna(how = "any")
dataframe_metricas.to_csv("dataframe_metricas.csv")