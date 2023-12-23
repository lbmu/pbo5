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
            buyerMenu()
            pass
        pass
    # print(mainMenu)
    # outputValue(data['penerbangan'])
    # outputValue(data['armada'])
    # outputValue(data['rute'])

    pass


if __name__ == '__main__':
    main()
