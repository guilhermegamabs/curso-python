"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
 descrito, exiba a saudação apropriada. Ex:
 Bom dia 0-11, Boa tarde 12-17, Boa Noite 18-23
"""

saudacao_str = input('Digite uma hora: ')

try:

    saudacao_int = int(saudacao_str)
    
    if(saudacao_int >= 0 and saudacao_int <= 11):
        print('Bom Dia!')
    elif(saudacao_int >= 12 and saudacao_int <= 17):
        print('Boa Tarde!')
    elif(saudacao_int >= 18 and saudacao_int <= 23):
        print('Boa Noite!')
    else:
        print(f'Não sei a saudação apropriada para essa hora: {saudacao_int}')
except:
    print('Valor digitado não é válido')