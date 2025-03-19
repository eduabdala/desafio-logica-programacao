"""
Módulo que calcula a soma acumulativa de números inteiros de 1 até o valor de INDICE.
O cálculo é realizado utilizando uma função que soma os números sucessivamente 
até o índice fornecido.
"""

INDICE = 13
SOMA = 0
K = 0

def calcular_soma(indice):
    """
    Calcula a soma acumulativa dos números de 1 até o valor de INDICE.
    
    Parâmetros:
        indice (int): O número até onde a soma deve ser calculada.
    
    Retorno:
        int: O valor final da soma.
    """
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

RESULTADO = calcular_soma(INDICE)
print("Valor final de SOMA:", RESULTADO)
