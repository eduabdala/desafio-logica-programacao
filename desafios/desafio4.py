"""
Módulo que calcula e exibe o percentual de participação no faturamento total 
de diferentes estados.
O código recebe um dicionário com os faturamentos de diferentes estados e calcula 
o percentual que cada um representa
em relação ao faturamento total, exibindo os resultados formatados.
"""

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

percentuais = {
    estado: (valor / faturamento_total) * 100
    for estado, valor in faturamento_estados.items()
}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
