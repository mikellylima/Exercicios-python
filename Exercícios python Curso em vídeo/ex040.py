print('Programa para cálculo da média e indicação de aprovação, reprovação ou recuperação')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2)/2
if m < 5:
    print('Sua média foi {}, está REPROVADO.'.format(m))
elif (m >= 5) and (m <= 6.9):
    print('Sua média foi {}, está em RECUPERAÇÃO.'.format(m))
elif m >= 7:
    print('Sua média foi {}, está APROVADO.'.format(m))