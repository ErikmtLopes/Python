#booleano
print(42 == 90)
print(2 != 3)
print(5 > 10)

#Operadores binarios (precisam de dois valores)
#and e or (operadores binarios)
print('_'*5)
#Se ambos os valores forem true o operador "and" considera True
print(True and True)
#Caso contrário "and" os considera False
print(True and False)
print(False and False)

#Por outro lado o operador "or" considera True se um dos valores forem True
print('_'*5)
print(True or False)
print(True or True)
print(False or False)

#Operador "Not" só atua sobre um valor booleano ou uma expressão.
#"Not" é simplesmente o valor booleano oposto
print('_'*5)
print(not True)
print(not False)
print(not not not not True)
print('_'*5)

#Misturando operadores booleanos e de comparação
print(4 < 5) and (5 < 6)
print(4 < 5) and (9 < 6)
print(1 == 2) or (2 == 2) 
 
