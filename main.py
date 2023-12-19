from menuProgram import *

mainMenu = None
while mainMenu != 'k':
    mainMenu = input('Login sebagai\n'
                     '[A]dmin | '
                     '[M]anajer | '
                     '[C]ustomer\n'
                     '======\n[K]eluar\n').lower()
    if mainMenu == 'a':
        adminMenu(input('Username : '), input('Password : '))
        pass
    elif mainMenu == 'm':
        managerMenu(input('Username : '), input('Password : '))
        pass
    elif mainMenu == 'c':
        buyerMenu(input('Username : '), input('Password : '))
        pass
# print(akun)
# print(akun['manajer'][0])

print()
