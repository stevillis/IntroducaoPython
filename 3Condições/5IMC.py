peso = float(input('Informe seu peso (Kg): '))
altura = float  (input('Informe sua altura (m): '))

imc = peso / altura**2

if imc < 18.5:
    classificação = 'Magreza'
else:
    if imc >= 18.5 and imc < 24.9:
        classificação = 'Normal'
    else:
        if 24.9 <= imc < 30:
            classificação = 'Sobrepeso'
        else:
            if imc >= 30:
                classificação = 'Obesidade'
print('\nClassificação: ' + classificação)
