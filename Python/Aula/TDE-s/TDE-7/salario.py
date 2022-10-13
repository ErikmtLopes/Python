#faça um algoritmo perguntando o salario total, e quanto do 
#salario ela gasta com besteira, e o quanto ela tem de gasto fixo. 
#retorne a porcentagem do salario que ela gasta em cada coisa.
#se o gasto com besteira for acima de 15%
#retorne a mensagem "Gasto acima do permitido".
#caso seja abaixo retorne "parabéns, continue economizando"

from unittest import result


salariot = float(input('Qual o seu salario? '))
gastof = float(input('Quanto você tem de gasto fixo? '))
gastob = float(input('Quanto você gasta com besteira? '))

porcentagem = salariot * 0.15
result2 = gastof*100/salariot
result3 = gastob*100/salariot

print ('%',result2)
print ('%',result3)
if gastob > porcentagem:
    print('gasto acima do permitido')
else:
    print('Parabéns, continue economizando')