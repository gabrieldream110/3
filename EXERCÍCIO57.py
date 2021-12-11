# Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

M = 'M'
F = 'F'
sexo = str(input('Gênero (M) ou (F): ')).upper().strip()
while sexo != M and sexo != F:
    print('Opção inválida.')
    sexo = str(input('Escolha entre (M) e (F): ')).upper().strip()
if sexo == 'M':
    print('Sexo Masculino.')
elif sexo == 'F':
    print('Sexo Feminino.')
