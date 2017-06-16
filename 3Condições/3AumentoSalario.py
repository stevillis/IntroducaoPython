salário = float(input('Informe o salário: '))

if salário > 1250:
    aumento = salário*10/100
if salário <= 1250:
    aumento = salário*15/100

print('O aumento sera de R$ %.2f' % (aumento))

