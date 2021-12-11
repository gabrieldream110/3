# Desafio 050: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
s  = 0
co = 0
for n in range(1,7):
    c = int(input('Digite um número inteiro:'))
    if c % 2 == 0:
        co += 1
        s += c
print('O somatório dos {} números pares digitados é igual a {}'.format(co,s))
