import numpy as np
import pandas as pd

dados = pd.read_json("dados.json")

# O menor valor de faturamento ocorrido em um dia do mês;

valores = dados.loc[dados['valor'] != 0.0]
menor_valor = min(valores['valor'])
print('Menor valor: ', menor_valor)
print('----------------------')

# O maior valor de faturamento ocorrido em um dia do mês;
maior_valor = max(valores['valor'])
print('Maior valor: ', maior_valor)
print('----------------------')

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
media = np.mean(valores['valor'])
print('Número de dias que o faturamento foi superior a média: ', valores.loc[valores['valor'] > media].shape[0])
