#Ler dois valores: num1 e num2, e se n1 for maior que n2, execute a soma
#caso contrário, execute uma subtração 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    soma = n1+n2
    print(soma)
elif n1 == n2:
    print('Números iguais')
else: 
    sub = n1-n2
    print(sub)
    