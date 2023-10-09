"""
Faça um programa que peça ao usuário para digitar um número inteiro
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""

numero_str = input("Digite um número inteiro: ")

if numero_str.isdigit():
    numero_int = int(numero_str)
    if(numero_int % 2 == 0):
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é ímpar')
else:
    print(f'Valor digitado não é inteiro: {numero_str}')    