lista = [1, 1, 2, 3, 5, 8, 11]
contador = 0
num_pesq = int(input('Número a pesquisar na lista: '))

for x in lista:
    contador += 1
    if x == num_pesq:    
        print('%d encontrado na posição: %d' % (num_pesq, contador))
        break
else:
    print('%d não encontrado na lista!' % num_pesq)
