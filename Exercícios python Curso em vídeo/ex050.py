print('Ler 6 números inteiros e somar os pares')
i = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        i += n
        cont += 1
print(f'Você informou {cont} valores pares e a soma dos mesmos é igual a {i}.')
