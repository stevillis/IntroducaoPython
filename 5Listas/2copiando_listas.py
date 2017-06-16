lista1, lista2, lista3 = [], [], []

print('Adicionando elementos na primeira lista.')
for x in range(0, 3):
    num = int(input('Digite um número: '))
    lista1.append(num)

print('\nAdicionando elementos na segunda lista.')
for x in range(0, 3):
    num = int(input('Digite um número: '))
    lista2.append(num)
    
print('\nCopiando elementos da primeira para a terceira lista.')
for x in range(0, 3):
    lista3.append(lista1[x])

print('\nCopiando elementos da segunda para a terceira lista.')
for x in range(0, 3):
    lista3.append(lista2[x])

print('\nPrimeira lista: ', lista1)
print('Segunda lista:', lista2)
print('Terceira lista: ', lista3)

"""
lista3 = lista1[:]
lista3+= lista2[:]
print(lista3)
"""


    

