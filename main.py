from menuProgram import *


def main():
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
        pass
    pass


if __name__ == '__main__':
    main()
