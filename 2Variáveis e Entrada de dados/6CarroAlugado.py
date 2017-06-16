km_percorridos = float(input('Quantidade de km percorridos: '))
qntd_dias = int(input('Quantidade de dias de aluguel: '))

preço = qntd_dias*60 + 0.15*km_percorridos

print('Preço a pagar: R$ {:.2f}'.format(preço))
