lista1, lista2, lista3 = [], [], []

for x in range(0, 3):
    num = int(input('Digite um número (lista 1): '))
    lista1.append(num)

for x in range(0, 3):
    num = int(input('Digite um número (lista 2): '))
    lista2.append(num)

for x in range(0, 3):
    if lista1[x] in lista3:
        pass
    else:
        lista3.append(lista1[x])

for x in range(0, 3):
    if lista2[x] in lista3:
        pass
    else:
        lista3.append(lista2[x])

print(lista3)
