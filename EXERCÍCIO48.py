# Desafio 048: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# Obs: para saber quantos laços o comando fez basta inserir, dentro da indetação de for, o comando:
# print('.') e ele conta quantos laços foram feitos até exibir a resolução proposta.

s = 0
co = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s  += c
        co += 1
print('A soma entre todos os {} números que são múltiplos de 3, no intervalo de 1 a 500 é igual a {}'.format(co,s))

