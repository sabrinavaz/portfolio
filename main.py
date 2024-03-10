#!pip install pandas scikit-learn

import pandas as pd

tabela = pd.read_csv("clientes.csv")
print(tabela)
print(tabela.info()) #mostrar null values, data type...

#codificar colunas da base de dados

from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

tabela["profissao"] = codificador.fit_transform(tabela["profissao"])

tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])

tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

#quem quero prever, quem quero usar pra fazer a previsao

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"]) #nome das colunas que quero excluir

#treino (60%-80%) e teste (20%-40%)

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

#criar I.A., Arvore de decisao, KNN, Nearest Neighbors

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

#treina a I.A.

modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

#testar os modelos

previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))

#escolher qual modelo é melhor

tabela_nova = pd.read_csv("novos_clientes.csv")
print(tabela_nova)

tabela_nova["profissao"] = codificador.fit_transform(tabela_nova["profissao"])
tabela_nova["mix_credito"] = codificador.fit_transform(tabela_nova["mix_credito"])
tabela_nova["comportamento_pagamento"] = codificador.fit_transform(tabela_nova["comportamento_pagamento"])

previsoes = modelo_arvoredecisao.predict(tabela_nova)
print(previsoes)