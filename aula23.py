"""
Try/Except

"""

numero_str = input('Dobrar o número:')

# print(numero_str.isdigit())

# numero_int = float(numero_str)
# print(f'O dobre de {numero_str} é {numero_int * 2:.1f}')

try:
    numero_int = float(numero_str)
    print(f'O dobre de {numero_str} é {numero_int * 2:.1f}')
except:
    print('Isso não é um número')