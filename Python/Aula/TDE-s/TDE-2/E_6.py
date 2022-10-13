#6. FUA para ler dois inteiros (variáveis A e B) e efetuar as operações de adição,
# subtração, multiplicação e divisão de A por B apresentando ao final os quatro resultados
# obtidos.

print('Para ter o resultados de 2 números nas 4 operações de aritimetica basica, faça como o algoritmo pede: ')
n1 = input('Digite um número inteiro: ')
n2 = input('Digite um número inteiro novamente: ')

soma = int(n1) + int(n2)
sub = int(n1) - int(n2)
mult = int(n1) * int(n2)
div = int(n1) / int(n2)

print('Os respectivos resultados é de')
print('Soma =',soma)
print('Subtração = ',sub)
print('Multiplicação=',mult)
print('Divisão',div)