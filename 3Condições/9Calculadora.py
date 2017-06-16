num1 = float(input('Informe o primeiro número: '))
operação = input('Informe a operação: (+, -, * ou /): ')
num2 = float(input('Informe o segundo número: '))

if operação == '+':
    resultado = num1 + num2
elif operação == '-':
    resultado = num1 - num2
elif operação == '*':
    resultado = num1 * num2
elif operação == '/':
    if num2 == 0:        
        resultado = 'Divisão por zero!'
    else:
        resultado = num1 / num2
else:
    resultado = 'Operação inválida!'

if resultado == 'Divisão por zero!':
    print(resultado)
elif resultado == 'Operação inválida!':
    print(resultado)
else:
    print('{} {} {} = {}'.format(num1, operação, num2, resultado))
