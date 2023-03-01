name = input('Quem é você? ').lower()
idade = int(input('Quantos anos você tem mesmo? '))

if name != ('alice'):
    print('Hello there, stranger one')
elif idade < 12:
    print("You're not Alice, kiddo")
elif idade > 999:
    print("Unlike you, Alice isn't a undead, imortal vampire")   
elif idade > 80:
   print("You're not Alice, grannie")
else:
    print('Hi Alice, welcomeback!!!')

