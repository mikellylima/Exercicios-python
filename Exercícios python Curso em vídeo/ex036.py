print('Programa para aprovação de empréstimo')
v = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual é o seu salário? R$ '))
a = int(input('Em quantos anos de financiamento? '))
prestacao = v/(a * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação terá um valor de {:.2f}.'.format(v, a, prestacao))
if prestacao > (s*0.3):
    print('Seu empréstimo foi negado!')
else:
    print('Parabéns, seu empréstimo foi aceito!')
