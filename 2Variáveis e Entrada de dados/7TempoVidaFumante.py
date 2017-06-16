qntd_cigarros = int(input('Quantidade de cigarros por dia: '))
qntd_anos = int(input('Quantidade de anos fumando: '))

total_cigarros = qntd_anos * 365 * qntd_cigarros
dias_vida = total_cigarros*10/1440

print('Dias de vida perdidos:', int(dias_vida))
