"""
Módulo que realiza a análise do faturamento de um conjunto de dados, 
que está armazenado em um arquivo JSON.
O código lê os dados do arquivo, filtra os valores positivos, 
calcula o menor e o maior faturamento, a média mensal
e o número de dias em que o faturamento foi superior à média mensal.
"""

import json

with open("data/dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

faturamento_filtrado = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print("Menor faturamento:", menor_faturamento)
print("Maior faturamento:", maior_faturamento)
print("Dias acima da média:", dias_acima_da_media)
