#8. Uma loja de animais precisa de um algoritmo para calcular os custos de criação de
# coelhos. O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. O
# algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.

nc = input ('Para calcular os custos de criação dos coelhos, digite o número de coelhos ')

custo = float( float (nc) * float (0.70)) / float(18+10)

print('O custo é de',custo)