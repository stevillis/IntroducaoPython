"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

anterior = 0
atual = 1

num = int(input('Informe a quantidade de termos da sequência\
de Fibonacci: '))

if num == 0:
    pass
elif num == 1:
    print(0, end=' ')
elif num == 2:
    print(0, 1, end=' ')
elif num > 2:
    print(0, 1, end=' ')    

    for x in range(0, num - 2):
        próximo = anterior + atual
        anterior = atual
        atual = próximo

        print(atual, end=' ')    
else:
    print('Precisa ser um número inteiro positivo!')

    
