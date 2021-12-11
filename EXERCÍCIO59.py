# Desafio 059: Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
m1 = 'A soma entre {} e {} é igual a {}'.format(n1,n2,(n1 + n2))
m2 = 'O produto entre {} e {} é igual a {}'.format(n1,n2,(n1 * n2))
menu = int(input('Escolha uma das operações abaixo:\n'
                 '[1] somar\n'
                 '[2] multiplicar\n'
                 '[3] maior\n'
                 '[4] novos números\n'
                 '[5] sair do programa\nOpção: '))
while menu < 5:
    if menu == 1:
        print(m1)
        menu = int(input('Escolha outra opção: '))
    elif menu == 2:
        print(m2)
        menu = int(input('Escolha outra opção: '))
    elif menu == 3:
        if n1 > n2:
            m3 = 'O maior número é {}'.format(n1)
        else:
            m3 = 'O maior número é {}'.format(n2)
        print(m3)
        menu = int(input('Escolha outra opção: '))
    elif menu == 4:
        while menu == 4:
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite um segundo valor: '))
            m1 = 'A soma entre {} e {} é igual a {}'.format(n1, n2, (n1 + n2))
            m2 = 'O produto entre {} e {} é igual a {}'.format(n1, n2, (n1 * n2))
            menu = int(input('Escolha uma das operações abaixo:\n'
                             '[1] somar\n'
                             '[2] multiplicar\n'
                             '[3] maior\n'
                             '[4] novos números\n'
                             '[5] sair do programa\nOpção: '))
print('Saiu do programa.')
