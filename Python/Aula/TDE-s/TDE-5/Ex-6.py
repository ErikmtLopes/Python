#Ler 3 números. Se o primeiro for positivo, imprima a sua raiz quadrada, caso contrário imprima seu quadrado.
#Se o segundo número for maior que 10 e menor que 100, imprima a msg "Número está entre 10 e 100 - intervalo
#permitido.
#Se o terceiro número for menor que o segundo, calcular e escrever a difenreça entre eles, caso contrário
#calcular e escrever a soma entre eles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
if n1 > 0:
    raiz = n1**0.5
    print(raiz)
elif n1 == 0:
    print('Esse número é 0.')
else:
    quadrado = n1**2
if n2 >= 10 and n2 <= 100:
    print('Intervelao permitido.')
else:
    print('Intervalo invalido.') 
if n3 < n2:
    dif = n3-n2
    print(dif)
elif n3 > n2:
    soma = n3+n2
    print(soma)
else:
    print('Os números são iguais.')

