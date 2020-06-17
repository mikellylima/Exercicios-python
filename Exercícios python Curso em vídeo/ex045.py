from random import randint
from time import sleep
import emoji
print('\033[31m-=-' * 10)
print('\033[1;7m     VAMOS JOGAR JOKENPÔ!!    \033[m')
print('\033[31m-=-\033[m' * 10)

print(emoji.emojize('[0] Pedra :new_moon:'))
print(emoji.emojize('[1] Papel :page_facing_up:'))
print(emoji.emojize('[1] Tesoura :scissors:'))

itens = ('PEDRA', 'PAPEL', 'TESOURA')
escolha = int(input('\033[1;36mQual a sua opção? '))
print('\033[1;7m   JO    \033[m', end='')
sleep(0.5)
print('\033[1;7m   KEN    \033[m', end='')
sleep(0.5)
print('\033[1;7m   PÔ!!    \033[m')
sleep(0.5)
pc = randint(0, 2)
print('\033[31m-=-' * 10)
print(f'\033[1;33mComputador jogou {itens[pc]}')
print(f'\033[1;33mJogador jogou {itens[escolha]}')
print('\033[31m-=-\033[m' * 10)
if escolha == pc:
    print(f'{itens[pc]} é igual a {itens[escolha]}')
    sleep(1)
    print('\033[1;7m           EMPATADO!          \033[m')
elif escolha == 0:
    if pc == 1:
        print('PAPEL engole PEDRA')
        sleep(1)
        print('\033[1;7m      COMPUTADOR VENCEU!      \033[m')
    elif pc == 2:
        print('PEDRA esmaga TESOURA')
        sleep(1)
        print('\033[1;7m        JOGADOR VENCEU!       \033[m')
elif escolha == 1:
    if pc == 0:
        print('PAPEL engole PEDRA')
        sleep(1)
        print('\033[1;7m        JOGADOR VENCEU!       \033[m')
    elif pc == 2:
        print('TESOURA corta PAPEL')
        sleep(1)
        print('\033[1;7m      COMPUTADOR VENCEU!      \033[m')
elif escolha == 2:
    if pc == 0:
        print('PEDRA esmaga TESOURA')
        sleep(1)
        print('\033[1;7m      COMPUTADOR VENCEU!      \033[m')
    elif pc == 1:
        print('TESOURA corta PAPEL')
        sleep(1)
        print('\033[1;7m        JOGADOR VENCEU!       \033[m')
else:
    print('Opção inválida, tente novamente!')
print('\033[31m-=-' * 10)
sleep(1)
print('\033[7;31m         FIM DE JOGO!         \033[m')
