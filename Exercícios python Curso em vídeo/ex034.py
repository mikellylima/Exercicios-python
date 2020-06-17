s = float(input('Digite o seu salário: R$ '))
if s > 1250:
    s = s*1.1
    print('Se salário com aumento de 10% é de R$ {:.2f}.'.format(s))
else:
    s = s*1.15
    print('Se salário com aumento de 15% é de R$ {:.2f}.'.format(s))
