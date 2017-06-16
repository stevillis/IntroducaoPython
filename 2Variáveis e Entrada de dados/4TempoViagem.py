# leitura da distância a percorrer
distância = float(input('Informe a distância a percorrer (km): '))

# leitura da velocidade média
velocidade_média = float(input('Informe a velocidade média(km/h): '))

# velocidade média = distância / tempo
tempo = distância/velocidade_média

print('Distância a percorrer: {} km\nVelocidade média: {} km/h\n\
Tempo a ser gasto: {} horas'.format(distância, velocidade_média, tempo))
