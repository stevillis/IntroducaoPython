leitura = int(input('Digite um número (0 para sair): '))
qntd_numeros = 0
soma = 0


while leitura != 0:
    qntd_numeros += 1
    soma += leitura

    leitura = int(input('Digite um número(0 para sair): '))

print('\nQuantidade de números digitados:', qntd_numeros)
print('Soma dos números digitados:', soma)
print('Média dos números digitados:', soma / qntd_numeros)
    
