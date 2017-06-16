num = int(input('Digite um número (0 para sair): '))

maior_num = num
menor_num = num
soma = 0

lista_num = []

while num != 0:
    if num >= maior_num:
        maior_num = num
    if num <= menor_num:
        menor_num = num

    lista_num.append(num)

    num = int(input('Digite um número (0 para sair): '))

for contador in lista_num:
    soma += contador

media = soma / len(lista_num)

print('\nMaior número: {}'.format(maior_num))
print('Menor número: {}'.format(menor_num))
print('Quantidade de números: {}'.format(len(lista_num)))
print('Soma dos números: {}'.format(soma))
print('Media dos números: {:.4f}'.format(media))
    

    
