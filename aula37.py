# string = 'ABCDE'

# lista = [123, True, 'Gui', 1.23]
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [1, 2, 3, 4, 5]

# lista[1] = 200
# print(lista)

# del lista[1]
# print(lista)

# """Remove o último valor da lista (Podemos passar índice no pop)"""
# lista.append(600)
# print(lista)
# lista.pop(3)

# """Adiciona no final da lista"""
# lista.append(700)
# print(lista)

# lista = [1, 2, 3, 4, 5]
# lista.insert(0, 10)
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

lista_a.extend(lista_b)

print(lista_c)
print(lista_a)