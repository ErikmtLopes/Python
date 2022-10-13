#Ler dois números. Se os números forem iguais, imprimir a msg "Números iguais"
#e encerrar a execução, caso contrário, imprimir o de maior valor.

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
if n1 == n2:
    print('Esses números são iguais. ')
elif n1 > n2:
    print (n1)
else:
    print (n2)
