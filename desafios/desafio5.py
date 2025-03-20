"""
Módulo que inverte os caracteres de uma string fornecida pelo usuário.
A função `reverse_string` recebe uma string e retorna a versão invertida dessa string, 
usando um método manual para inverter os caracteres.
"""

def reverse_string(s):
    """Inverte os caracteres de uma string manualmente."""
    inverted = ""
    for char in s:
        inverted = char + inverted
    return inverted

string_original = input("Digite uma string para inverter: ")

print("String invertida:", reverse_string(string_original))
