# Desafio 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# Fórmula para o enésimo termo: an = a1 + (n – 1) . r

t1 = int(input('Digite o valor do primeiro termo de uma Progressão Aritmética:'))
r  = int(input('Digite o valor da razão dessa mesma Progressão Aritmética:'))
n  = int(input('Digite o número de termos que deseja exibir na Progressão Aritmética:'))
s  = 0
c  = 0
for pa in range(t1,(t1 + (n*r)),+r):
    c += 1
    s += pa
    print(pa,end=' ')
print('\n\nEsta foi a PA até o {}°termo.'.format(c))
