# Desafio 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n  = int(input('Digite um valor inteiro:'))
co = 0
for c in range(1, n + 1):
    if n % c == 0:
        d = n / c
        co += 1

print('Divisões possíveis para {}: {}'.format(n, co))
if co == 2:
    print('O número {} é divisível apenas por 1 e por ele mesmo, portanto, é número primo.'.format(n))
else:
    print('O número {} é divisível por 4 ou mais números, portanto, não é número primo.'.format(n))
