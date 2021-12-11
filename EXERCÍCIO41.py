# Desafio 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

an = int(input('Ano de nascimento:'))
id = 2020 - an

if id < 10:
    print('Categoria: MIRIM.')
elif id > 9 and id < 15:
    print('Categoria: INFANTIL.')
elif id > 14 and id < 20:
    print('Categoria JÚNIOR.')
elif id > 19 and id < 26:
    print('Categoria: SÊNIOR.')
elif id > 25:
    print('Categoria: MASTER.')
