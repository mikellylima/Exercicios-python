from random import randint
from time import sleep
print('-=-' * 10)
print('Adivinhe o número que eu pensei...')
print('-=-' * 10)
n = randint(0, 5)
value = int(input('Digite um valor: '))
print('PROCESSANDO...')
sleep(2)
if n == value:
    print('Parabéns, você acertou o chute!')
elif n < value:
    print('Seu chute foi maior!')
elif n > value:
    print('Seu chute foi menor!')