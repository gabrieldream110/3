# Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

nomemv = 0
idade = 0
mulheres = 0
velho = 0
media = 0
total = 0
n = int(input('Número de participantes na avaliação:'))
for c in range(1,n +1):
    nome = str(input('Digite o nome da {}ª pessoa:'.format(c)).strip())
    idade = int(input('Digite a idade dessa pessoa:'))
    sexo = int(input('Masculino (10) ou Feminino (11)?'))
    total += idade
    media = total/n
    if sexo == 10:
        if c == 1:
            velho = idade
            nomemv = nome
        else:
            if idade > velho:
                velho = idade
                nomemv = nome
    if sexo == 11 and idade < 20:
        mulheres += 1
print('A média de idades registrada é igual a {}'.format(media))
print('{} é o homem mais velho e tem {} anos.'.format(nomemv,velho))
print('Há {} mulheres com idade inferior a 20 anos.'.format(mulheres))
