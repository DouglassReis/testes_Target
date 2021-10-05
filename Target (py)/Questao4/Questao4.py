import pandas as pd

dataFrame = pd.read_json('faturamento.json')
faturamento_total = sum(dataFrame['valor'])
valores_faturamento = dataFrame['valor']
i = 0
for valor in valores_faturamento:
    valores_percentuais = (valores_faturamento / faturamento_total)*100
    i += 1
dataFrame = dataFrame.assign(percentual = [
                                      "%.2f" % valores_percentuais[0],
                                      "%.2f" % valores_percentuais[1],
                                      "%.2f" % valores_percentuais[2],
                                      "%.2f" % valores_percentuais[3],
                                      "%.2f" % valores_percentuais[4]
                                     ])
print(dataFrame)