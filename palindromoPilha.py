import re

# Exercício 1 - Pilha 

def eh_palindromo(texto):
    # 1º Normalização: remove espaços, pontuação e ignora maiúsculas
    texto_normalizado = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()

    pilha = []

    # 2º Empilha todos os caracteres
    for caractere in texto_normalizado:
        pilha.append(caractere)

    texto_invertido = ""

    # 3º Desempilha para formar o texto invertido
    while pilha:
        texto_invertido += pilha.pop()

    # 4º Compara o texto normal com o invertido
    return texto_normalizado == texto_invertido

texto_usuario = input("Digite uma palavra ou frase: ")

if eh_palindromo(texto_usuario):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")