while True:
    name = input('Who are you? ')
    if name != 'Yugi':
        continue
    print('Hello Yugi, whats the password? ')
    password = input('Type the password (it is a card): ')
    if password == 'Dark Magician':
        break
print('Acess granted!')
print('Welcomeback King')