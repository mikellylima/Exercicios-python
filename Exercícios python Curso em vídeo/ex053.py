print('Ler uma frase e saber se é palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
print(len(juntar))
inverso = ''
# inverso = juntar[::-1] // Outra forma de se fazer sem a utilização do for
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print(f'A frase {juntar} e seu inverso {inverso} são iguais, logo é um palíndromo.')
else:
    print(f'A frase não é um palíndromo.')
