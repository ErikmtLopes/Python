#11.F.U.A que leia dois números e calcule qual é o resto da divisão do 1o pelo 2o número.
# Exiba na tela este valor final.

n1 = input ('Digite o primeiro número: ')
n2 = input ('Digite o segundo: ')

div = float (n1) / float (n2)
rdiv = float (n1) % float (n2)

print ('A divisão do número é de',div,'e o restante da divisao é',rdiv)