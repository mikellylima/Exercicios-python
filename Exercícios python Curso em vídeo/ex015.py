d = int(input('Digite a quantidade de dias do aluguel do carro: '))
km = float(input('Digite a quantidade de km rodados: '))
r = (60*d)+(km*0.15)
print('O valor total do aluguel é de R$ {:.2f}.'.format(r))
