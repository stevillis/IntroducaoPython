"""
    |a11    a12|
A = |          |
    |a21    a22|

det A = a11*a22 - a21*a12
"""

a11 = float(input('a11: '))
a12 = float(input('a12: '))
a21 = float(input('a21: '))
a22 = float(input('a22: '))

matriz = [[a11, a12],
          [a21, a22]]

determinante = matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1]

for i in matriz:
    print(i)

print('Determinante = %.2f' % (determinante))

