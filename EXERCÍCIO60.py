# Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial

n = int(input('Qual o fatorial de: '))
f = factorial(n)
x = 0
print('\nResposta: \n')

while n > 1:
    n = n - 1
    print(n + 1,'X', end=' ')
print(1,' : ',f)
print('\nO Fatorial é igual a : {}'.format(f))