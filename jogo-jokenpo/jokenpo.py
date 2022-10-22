from random import randint
from time import sleep
acertou = False
tentativas = 0
computador = int(randint(0, 10))
print('='*40)
print('\033[32m{:*^40}\033[m'.format(' Jogo da adivinhação '))
print('='*40)
sleep(2)
print('\033[36mOlá! Sou seu computador...')
sleep(2)
print('Vou pensar em um número de 0 a 10')
sleep(2)
print('Será que você consegue adivinhar?')
sleep(2)
print('\033[35mPENSANDO...')
sleep(3)
print('\033[36mPronto, sua vez...')
sleep(2)
while not acertou:
    chute = int(input('\033[30mDigite um número de 0 a 10: '))
    while chute not in range(0, 11):
        chute = int(input('\033[31mDados inválidos, tente novamente: \033[30m'))
    tentativas += 1
    if chute == computador:
        acertou = True
    else:
        if chute > computador:
            print('Menos...tente novamente...')
        elif chute < computador:
            print('Mais...tente novamente')
print('\n\033[34mParabéns, pensei no número {}.\nVocê acertou e precisou de {} tentativa(s).'.format(computador, tentativas))
