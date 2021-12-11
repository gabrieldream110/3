# Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random

pedra   = 0
rede    = 1
tesoura = 2

r  = 'Rede cobre pedra'
t  = 'Tesoura corta rede'
p  = 'Pedra amassa tesoura'

es = (0,1,2)

eu = int(input('Jokenpo!!!\nRegras:\n'
               '\n0 = Pedra'
               '\n1 = Rede'
               '\n2 = Tesoura'
               '\nAgora escolha um número pra começarmos a jogar:'))
pc = random.choice(es)

if eu == pc:
    print('Deu empate. Vamos jogar de novo.')
elif eu > 2:
    print('Resposta inválida. As opções são de 0 a 2.')
elif eu == 0 and pc == 1:
    print('{} Eu ganhei!!!'.format(r))
elif eu == 1 and pc == 0:
    print('{} Aff. Você ganhou.'.format(r))
elif eu == 1 and pc == 2:
    print('{} Eu ganhei!!!'.format(t))
elif eu == 2 and pc == 1:
    print('{} Aff. Você ganhou.'.format(t))
elif eu == 0 and pc == 2:
    print('{} Aff. Você ganhou.'.format(p))
elif eu == 2 and pc == 0:
    print('{} Eu ganhei!!!'.format(p))
