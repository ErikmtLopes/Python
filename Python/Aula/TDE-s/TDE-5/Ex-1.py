#Dados dois números A e B, some 100 ao maior número e imprima

A = input('Digite o valor de A: ')
B = input('Digite o valor de B: ')
if A>B:
    maior = int(A) + 100
    print (maior)
else:
    maior = int(B) + 100
    print (maior)