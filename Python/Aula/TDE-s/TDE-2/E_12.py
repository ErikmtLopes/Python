#12. F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o
# número. Exiba na tela este valor final.

n1 = input ('Digite o valor do primeiro número: ')
n2 = input ('Digite o valor do segundo número: ')

div1 = float (n1) / float (n2)
div2 = float (n2) / float (n1)

print('O valor da divisão do 1º pelo 2º número é:',div1)
print('E o valor da divisão do 2º pelo 1º número é:',div2)