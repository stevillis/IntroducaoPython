# leitura da temperatura em ºC
celsius = float(input('Temperatura em ºC: '))

# Tc    Tf - 32
# --- =  -------
#  5        9

fahrenheit = (9 * celsius)/5 + 32

print('Temperatura em ºF:', fahrenheit)
