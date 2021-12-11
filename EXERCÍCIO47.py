# Desafio 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# O que eu aprendi: Para que o programa execute menos repetições, economizando na memória do computador,
# preciso realizar a contagem de 2 em 2 para o programa ter menos trabalho.
# O comando end=' ' exibe os números em sequência da esquerda para a direita, um na frente do outro.

import time
for c in range(2,51,2):
    print(c,end=' ')
    time.sleep(0.25)
print('Fim')
