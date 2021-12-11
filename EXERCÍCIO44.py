# Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

p  = float(input('Valor do produto:'))
fp = int(input('Forma de pagamento:\n'
           '(0)À vista (dinheiro/cheque) (1) À vista (cartão) (2)2 x cartão (3)3x cartão:\nDigite um número:'))
av  = p - (p*(10/100))
avc = p - (p*(5/100))
c2x = p*1
c3x = p + (p*(20/100))

if fp == 0:
    print('Selecionado à vista (dinheiro/cheque) com 10% de desconto. Valor final R$ {}'.format(av))
elif fp == 1:
    print('Selecionado à vista no cartão com 5% de desconto. Valor final R$ {}'.format(avc))
elif fp == 2:
    print('Selecionado em 2x no cartão, preço normal. Valor final R$ {}'.format(c2x))
elif fp == 3:
    print('Selecionado no cartão em 3x com 20% de juros. Valor final R$ {}'.format(c3x))

