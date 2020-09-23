print('Recebe o peso de 5 pessoas e indica qual o maior e qual o menor peso')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa(kg): '))
    if p == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O maior peso lido foi de {maior} kg.')
print(f'O menor peso lido doi de {menor} kg.')
