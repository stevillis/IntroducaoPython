contador = int(input('Informe um número para a \
contagem regressiva: '))

if contador > 0:
    while contador >= 0:
        print(contador)
        contador = contador - 1
else:
    print('O número precisa ser maior que zero!')
