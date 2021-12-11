# Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
# Fórmula: peso dividido pela altura ao quadrado.

p   = float(input('Peso atual:'))
a   = float(input('Altura:'))
imc = p/(a**2)

if imc < 18.5:
    print('Imc: {:.2f} => Abaixo do peso.'.format(imc))
elif imc > 18.4 and imc < 25:
    print('Imc: {:.2f} => Peso ideal.'.format(imc))
elif imc > 24 and imc < 30:
    print('Imc: {:.2f}. Sobrepeso.'.format(imc))
elif imc > 29 and imc < 40:
    print('Imc: {:.2f} => Obesidade.'.format(imc))
elif imc > 40:
    print('Imc: {:.2f} => Obesidade mórbida.'.format(imc))
