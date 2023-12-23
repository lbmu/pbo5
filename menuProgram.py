from databasefunction import *
from classBuyer import *


def outputValue(val):
    for x in val:
        print(x)


def typo():
    print('typo bang')


def inputMenuPriv():
    return input("[T]ambah | "
                 "[H]apus | "
                 "[E]dit | "
                 "[O]utput | "
                 "[L]ainnya | "
                 "[K]eluar\n"
                 "--> ").lower()
    pass


def adminMenu(user, pin):
    # for i in range(len(akun['admin'])):
    if user in username['admin'] and len(user) != 0:
        if pin in password['admin']:
            print('adm priv')
            admin = Admin(username['manager'], password['manager'])     # objek admin untuk data manager
            inputMenuAdmin = None
            while inputMenuAdmin != 'k':
                if inputMenuAdmin == 't':
                    admin.tambahData()
                    pass
                elif inputMenuAdmin == 'h':
                    admin.hapusData()
                    pass
                elif inputMenuAdmin == 'e':
                    admin.editData()
                    pass
                elif inputMenuAdmin == 'o':
                    admin.outputData()
                    pass
                else:
                    typo()
                inputMenuAdmin = inputMenuPriv()
                pass
        else:
            print('Maaf salah username atau password')
            pass
    else:
        print('Maaf salah username atau password')
        pass
    pass


def managerMenu(user, pin):
    if user in username['manager'] and pin in password['manager']:
        print('manager priv')
        menu = None
        manager = Manager(data['penerbangan'], data['armada'], data['rute'], tiket)
        # manager.tiket = tiket
        while menu != 'k':
            if menu == 't':
                manager.tambahData()
                pass
            elif menu == 'h':
                manager.hapusData()
                pass
            elif menu == 'e':
                manager.editData()
                pass
            elif menu == 'o':
                manager.outputData()
                pass
            elif menu == 'l':
                manager.tiketData(tiket)

            menu = inputMenuPriv()
            pass

    else:
        print('Maaf salah username atau password')
    pass


def buyerMenu():
    print('Welcome to mobel lejeng')
    buyer = Buyer(data['penerbangan'], data['armada'], data['rute'], tiket)
    # buyer.tiket = tiket
    menu = None
    while menu != 'k':
        if menu == 'c':
            buyer.cariData()
            pass
        elif menu == 'd':
            buyer.outputData()
            pass
        elif menu == 'p':
            pass
        menu = inputMenuUser()
    pass
