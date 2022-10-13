nf = int(input('digite o número do funcionario: '))
nh = float(input('Digite o número de horas trabalhadas: '))
vh = float(input('Valor que recebe por hora: '))
nfi = int(input('Número de filhos com idade inferior a 14: '))
idade = int(input('Sua idade: '))
tempo = float(input('A quantos anos você trabalha na empresa: '))
vfs = float(input('Valor fixo do salario familia: '))

salariof = float(nfi*vfs) #salario familia
salariob = float((nh*vh)+(salariof)) #salario bruto
inss = salariob % 8.5

if salariob > 1500:
    impostore = salariob%15
elif salariob > 500 and salariob <= 1500:
    impostore = salariob%8
else:
    impostore = 0

totald = impostore + inss
salariol = salariob - totald 

print ('O salario bruto do funcionario', nf,'é de: ',salariob)
print ('O total de descontos é de',totald)
print ('salario liquido de ',salariol)
