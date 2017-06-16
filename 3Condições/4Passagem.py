distância = int(input('Distância a percorrer: '))

if distância <= 200:
    passagem = distância*0.5
else:
    passagem = distância*0.45

print('Valor da passagem: %.2f' % (passagem))
