alt = float(input('Digite a sua altura: '))
sexo = input('Você é Homem ou Mulher? ')
if sexo == 'homem' :
    peso = (72.7*alt)-58
    print(peso)
elif sexo == 'mulher':
    peso = (62.1*alt)-44.7
    print(peso)
else:
    print('Comando invalido')