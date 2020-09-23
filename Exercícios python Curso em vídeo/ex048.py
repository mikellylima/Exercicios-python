print('Calcular a soma de todos os números ímpares múltiplos de 3 de 1 a 500')
i = 0
j = 0
for c in range(0, 500):
    if c % 3 == 0:
        if c % 2 != 0:
            i += c
            j += 1
print(f'A soma dos {j} solicitados é igual a {i}')
