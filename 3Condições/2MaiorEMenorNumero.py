num = int(input('Primeiro número: '))

maior = num
menor = num

num = int(input('Segundo número: '))
if num > maior:
    maior = num
if num < menor:
    menor = num

num = int(input('Terceiro número: '))
if num > maior:
    maior = num
if num < menor:
    menor = num

print('O maior número é: %d\nO menor número é: %d' % (maior, menor))
