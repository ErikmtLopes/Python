#10.F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário
# o preço que ele tem que pagar pela compra.

pp = input ('Qual o preço do produto? ')
qc = input ('Qual a quanntidade que tu queres comprar? ')

pc = float (pp) * float (qc) 
print ('O preço da compra é de R$',pc)