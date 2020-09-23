print('Fazer os 10 primeiros termos de uma Progressão Aritmética')
a1 = int(input('Digite o termo a1 da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(1, 11):
    print(f'a{c} = {a1 + (c - 1)*r}')
