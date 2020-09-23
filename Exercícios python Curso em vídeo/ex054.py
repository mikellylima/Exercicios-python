from datetime import date
print('Indicação de maioridade de 7 pessoas por meio da data de nascimento')
i = 0
ii = 0
for c in range(1, 8):
    nascimento = int(input(f'Digite seu ano de nascimento da {c}ª pessoa: '))
    atual = date.today().year
    idade = atual - nascimento
    if idade < 18:
        i = i + 1
    elif idade >= 18:
        ii = ii + 1
print(f'{i} pessoas são de menor e {ii} pessoas são de maior.')