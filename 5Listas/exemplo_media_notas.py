lista = []
soma = 0
for x in range(0, 3):
    nota = float(input('Informe a %dª nota: ' % (x + 1)))
    lista.append(nota)

for x in range(0, len(lista)):
    soma += lista[x]

media = soma / len(lista)

print('\nMédia das notas: %.2f' % media)
    
