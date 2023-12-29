from databasefunction import *
# import databasefunction
from classBuyer import *


def outputValue(val):
    for x in val:
        print(x)


def typo():
    print('Maaf tidak valid')


def inputMenuPriv():
    return input("[T]ambah | "
                 "[H]apus | "
                 "[E]dit | "
                 "[O]utput | "
                 "[L]ainnya | "
                 "[K]eluar\n"
                 "--> ").lower()


def adminMenu(user, pin):
    # for i in range(len(akun['admin'])):
    if user in username['admin'] and len(user) != 0:
        if pin in password['admin']:
            print('Login sebagai')
            admin = Admin(username['manager'], password['manager'])     # objek admin untuk data manager
            inputMenuAdmin = None
            while inputMenuAdmin != 'k':
                inputMenuAdmin = inputMenuPriv()
                if inputMenuAdmin == 't':
                    admin.tambahData()
                    
                elif inputMenuAdmin == 'h':
                    admin.hapusData()
                    
                elif inputMenuAdmin == 'e':
                    admin.editData()
                    
                elif inputMenuAdmin == 'o':
                    admin.outputData()
                    
                else:
                    typo()
                
        else:
            typo()
            
    else:
        typo()
    

def managerMenu(user, pin):
    if user in username['manager'] and len(user) != 0:
        if pin in password['manager']:
            print('manager priv')
            menu = None
            manager = Manager(data['penerbangan'], data['armada'], data['rute'], tiket, cuan)
            # manager.tiket = tiket
            while menu != 'k':
                menu = inputMenuPriv()
                if menu == 't':
                    manager.tambahData()

                elif menu == 'h':
                    manager.hapusData()

                elif menu == 'e':
                    manager.editData()
                elif menu == 'o':
                    manager.outputData()

                elif menu == 'l':
                    manager.tiketData()

                else:
                    typo()


        else:
            print('Maaf salah username atau password')
    else:
        print('Maaf salah username atau password')


def buyerMenu(user, pin):
    print('Welcome to ZTravel')
    buyer = Buyer(data['penerbangan'], data['armada'], data['rute'], tiket, cuan, user)
    # buyer.tiket = tiket
    menu = None
    while menu != 'k':
        if menu == 'c':
            buyer.cariData()
            
        elif menu == 'd':
            buyer.outputData()
            
        elif menu == 'p':
            buyer.pesanTiket()
            
        menu = inputMenuUser()
    
