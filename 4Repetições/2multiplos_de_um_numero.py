num = int(input('Deseja os múltiplos do número: '))
multiplo = 0
contador = 0

print('\nOs 10 primeiros múltiplos de %d são:'%num)
while contador < 10:
    if multiplo % num == 0:
        print(multiplo, end=' ')
        contador += 1    
    multiplo += 1
