print('Cálculo do preço do produto de acordo com a condição de pagamento')
print('=' * 10, end='')
print(' LOJAS FARIAS ', end='')
print('=' * 10)
p = float(input('Digite o preço do produto: R$ '))
print("""FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
cod = int(input('Escolha a forma de pagamento: '))
if cod == 1:
    p = p - (p*0.1)
    print('O preço do produto à vista em dinheiro/cheque é de R${:.2f}'.format(p))
elif cod == 2:
    p = p - (p*0.05)
    print('O preço do produto à vista no cartão é de R${:.2f}'.format(p))
elif cod == 3:
    print('O preço do produto 2x no cartão é de R${:.2f} sem juros'.format(p))
elif cod == 4:
    p = p + (p * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = p/totalparc
    print('Sua compra será parccelada em {}x de R${:.2f} com juros.'.format(totalparc, parcela))
    print('O preço do produto {}x no cartão é de R${:.2f} com juros'.format(totalparc, p))
else:
    print('Opção de pagamento inválida, tente novamente!')