from menuProgram import *
# Konfirmasi metode (modul classAdmin, line 25)
# Estetika baris
# Perapihan Menu

# Menu untuk user memilih login "[A]dmin, [M]anajer, atau [C]ustomer"
def main(): 
    mainMenu = None
    while mainMenu != 'k':
        mainMenu = input('Login sebagai\n'
                         '[A]dmin | '
                         '[M]anajer | '
                         '[C]ustomer\n'
                         '======\n[K]eluar\n'
                         '--> ').lower()
        if mainMenu == 'a':
            adminMenu(input('Username : '), input('Password : '))
            
        elif mainMenu == 'm':
            managerMenu(input('Username : '), input('Password : '))
            
        elif mainMenu == 'c':
            buyerMenu(input('Username : '), input('Password : '))
        else :
            typo()


if __name__ == '__main__':
    main()
