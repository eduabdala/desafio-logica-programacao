""""
Módulo que verifica se um número pertence à sequência de Fibonacci.
A função is_fibonacci recebe um número e retorna True se ele estiver na sequência de Fibonacci,
caso contrário, retorna False.
"""
def is_fibonacci(n):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    A sequência de Fibonacci é uma série de números em que cada número é a soma dos dois anteriores,
    começando com 0 e 1. A função verifica se o número dado faz parte dessa sequência.
    
    Parâmetros:
        n (int): O número a ser verificado.
    
    Retorno:
        bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
