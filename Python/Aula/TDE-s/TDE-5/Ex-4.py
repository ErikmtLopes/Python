#Leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo
n1 = int(input('Digite um número: '))
if n1%2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')
if n1>0:
    print('Esse número é positivo.')
elif n1==0:
    print('O número não possui valor.')
else:
    print('O número é negativo.')