#Ler dois valores númericos e apresentar a diferença do maior pelo menor

A = int(input('Digite um número: '))
B = int(input('Digite outro número: '))
ma = A - B
mb = B - A
if A > B: 
    print(ma)
else:
    print(mb)