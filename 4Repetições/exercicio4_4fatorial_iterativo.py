num = int(input('Digite um número e calcularei o fatorial: '))

if num < 0:
    print('Precisa ser um número inteiro não negativo!')
else:
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i

    print('{}! = {}'.format(num, fatorial))
    
