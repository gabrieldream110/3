# Desafio 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.
# Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
a = 0
t = 0
lista = [1,2,3,4,5,6,7,8,9,10]
pc = random.choice(lista)
n = int(input('Digite o valor que você acha que eu pensei: '))
if n == pc:
    print('Parabéns!!! Você acertou.')
else:
    while n != pc:
        a += 1
        t = a + 1
        print('Errou!!!')
        n = int(input('Digite o número que você acha que eu pensei agora? '))
    print('Pensei em {}.'.format(pc))
    print('Até que fim você acertou ein! Mas precisou dar {} palpites até acertar.'.format(t))
