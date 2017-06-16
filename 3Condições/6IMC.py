peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso/altura**2

if imc < 18.5:
    classificação = 'Magreza'
elif imc >= 18.5 and imc < 24.9:
    classificação = 'Normal'
elif 24.9 <= imc < 30:
    classificação = 'Sobrepeso'
elif imc >= 30:
    classificação = 'Obesidade'
print('\nClassificação: ' + classificação)
    
