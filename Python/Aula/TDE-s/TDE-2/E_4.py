#Faça um algoritmo para calcular a média aritmética entre três números quaisquer.

print('Em sequencia, digite 3 valores (um por vez) para calcular a sua média')
n1 = input()
n2 = input()
n3 = input()

sn = float(n1) + float(n2) + float(n3)
mn = float(sn) / float(3)

print('A soma dos números é de', sn,'e a media é igual a',mn)