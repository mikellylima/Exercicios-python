print('Tabuada utilizando o laço for')
n = int(input('Digite o número: '))
print('-=-' * 3)
print(f'Tabuada dos {n}')
print('-=-' * 3)
for c in range(0, 11):
    print(f'{n} x {c} = {c*n}')
print('-=-' * 3)
