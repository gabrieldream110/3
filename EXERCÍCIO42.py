# Desafio 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a   = float(input('Primeiro segmento:'))
b   = float(input('Segundo segmento:'))
c   = float(input('Terceiro segmento:'))

c1  = a + b > c
c2  = a + c > b
c3  = b + c > a

# Equilátero:
eq  = a == b == c

# Isósceles:
is1 = a == b < c
is2 = a == b > c
is3 = a < b == c
is4 = a > b == c
is5 = a == c > b
is6 = a == c < b

# Escaleno:
es1 = a < b < c
es2 = a < b > c
es3 = a > b > c
es4 = a > b < c
es5 = a < c < b
es6 = a > c > b


print('Com os valores de segmento abaixo:\na: {}\nb: {}\nc: {}'.format(a,b,c))
if c1 is False or c2 is False or c3 is False:
    print('Não será possível formar um triângulo.')
elif c1 is True and c2 is True and c3 is True and a == b and a == c and b == c:
    print('Será possível formar um triângulo do tipo:\nEQUILÁTERO')
elif is1 or is2 or is3 or is4 or is5 or is6 is True:
    print('Será possível formar um triângulo do tipo:\nISÓSCELES')
elif es1 or es2 or es3 or es4 or es5 or es6 is True:
    print('Será possível formar um triângulo do tipo:\nESCALENO')
