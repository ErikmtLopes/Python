#5. Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas
# trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário
# deste funcionário.

nome = input('Digite seu nome: ')
print ('Olá', nome,'para calcular o seu salario, siga as instruções do algoritmo')

nf = input('Digite seu número de funcionario: ')
nh = input('Digite o número de horas trabalhadas no dia: ')
nd = input('Digite o número de dias que você trabalha: ')
vh = input('Digite o valor que você recebe por hora:')


sa = float (float(nh) * float(nd)) * float (vh)

print(nome,'cujo o código é', nf,'o seu salário é de:', sa)
