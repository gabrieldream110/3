# Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
idade = 0
hoje = 2020
menores = 0
maiores = 0

for pessoas in range(0, 7):
    ano = int(input('Ano de nascimento:'))
    idade = hoje - ano
    if idade > 17:
        maiores += 1
    elif idade < 18:
        menores += 1

print('Pessoas maiores de idade: {}'.format(maiores))
print('Pessoas menores de idade: {}'.format(menores))
