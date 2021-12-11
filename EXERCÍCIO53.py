# Desafio 053:  Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase:')).strip().upper()
divisao = frase.split()
junto = ''.join(divisao)
leia = len(junto)
inverso = ''
for letra in range(leia -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos que {} é igual a {}, portanto temos um palíndromo.'.format(inverso, junto))
else:
    print('Temos que {} é diferente de {}, portanto não é palíndromo.'.format(inverso,junto))
