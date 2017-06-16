velocidade = int(input('Velocidade (km/h): '))

if velocidade > 80:
    multa = (velocidade - 80)*5
    print('\nVocê foi multado!\nValor da multa R$: {}'.format(multa))
