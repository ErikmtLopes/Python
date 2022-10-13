#Ler dois valores e escreva cada um juntamente com a msg: "É multiplo de 2" ou "Não é multiplo de 2"

n1 = int(input('Digite um número: '))
n2 = int(input('Difite outro número: '))
if n1%2==0:
    print('O número',n1,'é multiplo de 2')
else:
    print('O número',n1,'não é multiplo de 2')
if n2%2==0:
    print('O número',n2,'é multiplo de 2')
else:
    print('O número',n2,'não é multiplo de 2')