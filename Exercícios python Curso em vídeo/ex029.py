v = int(input('Digite a velocidade do carro: '))
if v > 80:
    m = (v - 80)*7
    print('Você foi multado em R$ {:.2f} por excesso de velocidade!'.format(m))
else:
    print('Dirija dentro do limite estabelecido.')
