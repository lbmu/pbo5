from databasefunction import *
from classAdmin import *
from classManager import *
from classBuyer import *
# import database as db
# import database


def adminMenu(user, pin):
    # for i in range(len(akun['admin'])):
    if user == username['admin'] and pin == password['admin']:
        print('adm priv')
        admin = Admin(username['manager'], password['manager'])
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
            inputMenuAdmin = inputMenuPriv()
            pass
    else:
        print('Maaf salah username atau password')
        pass
    pass


def managerMenu(user, pin):
    if user in username['manager'] and pin in password['manager']:
        print('manager priv')
        manager = Manager(data['penerbangan'], data['armada'], tiket)
        menu = None
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
            menu = inputMenuPriv()
            pass

    else:
        print('Maaf salah username atau password')
    pass


def buyerMenu(user, pin):
    if user in username['user'] and pin in password['user']:
        print('Welcome to mobel lejeng')
        buyer = Buyer()
    else:
        print('Maaf salah username atau password')
    pass


