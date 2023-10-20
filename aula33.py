""" Calculadora com While """
pergunta = input('Deseja fazer a conta (S) Sim (N) Não: ').lower()

while(pergunta == 's'):
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    sinal = input('Digite um sinal operacional: ')

    numeros_validos = None
    try:
        num1_float= float(num_1)
        num2_float= float(num_2)
        numeros_validos = True
    except:
          numeros_validos = None

    if numeros_validos is None:
          print('Um ou ambos os números digitados são inválidos!')
          continue
    
    if(sinal == '+'):
            print(num1_float + num2_float)
    elif(sinal == '-'):
            print(num1_float - num2_float)
    elif(sinal == '/'):
            print(num1_float / num2_float)
    elif(sinal == '*'):
            print(num1_float * num2_float)
    else:
        print('Não existe essa operação no sistema ainda!')

    pergunta = input('Deseja fazer a conta (S) Sim (N) Não: ').lower()


    


print('ACABOU')