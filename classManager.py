from classAdmin import *
from databasefunction import inputMenuManager
from classTicket import Ticket, menuTiket


class Manager(Admin):
    def __init__(self, terbang, armada, tiket):
        super().__init__
        self._terbang = []
        self._depart = terbang[0]   # Departure
        self._arrive = terbang[1]   # Arrival
        self._armada = armada
        self._tiket = tiket
        self._dataTerbang = len(terbang)
        self._dataArmada = len(armada)
        self._dataTiket = len(tiket)
        self.__userQty = None
        pass

    def getData(self):
        return self

    @property
    def getTiket(self):
        return self._tiket

    @property
    def getTerbang(self):
        return self._terbang

    @property
    def getArmada(self):
        return self._armada

    def tambahData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                dataDepart = input('Departure : ')
                self._depart.append(dataDepart)
                dataArrive = input('Tujuan : ')
                self._arrive.append(dataArrive)

                self._terbang.append(dataDepart + ' - ' + dataArrive)
                self._dataTerbang += 1
            elif menu == 'a':   # Armada
                self._armada.append(input('Masukkan Data Armada\n--> '))
                self._dataArmada += 1
                pass
            print('Penambahan Data')
            menu = inputMenuManager()
        pass

    def hapusData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                # Penerbangan
                i = 1
                for x in self._terbang:
                    print(i, end='. ')
                    i += 1
                    print(x)
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._terbang.pop(pivot-1)
                pass
            elif menu == 'a':   # Armada
                for i in range(self._dataArmada):
                    print(f'{[i+1]}. {self._armada[i]}')
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._armada.pop(pivot-1)
            menu = inputMenuManager()

        pass

    def editData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':     # Penerbangan
                for i in range(self._dataTerbang):
                    print(f'{i+1}. {self._terbang[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._terbang[pivot-1] = input('Masukkan data baru\n')
                pass
            elif menu == 'a':   # Armada
                for i in range(self._dataArmada):
                    print(f'{i+1}. {self._armada[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._armada[pivot-1] = input('Masukkan data baru\n')
                pass
            menu = inputMenuManager()
        pass

    def tiketData(self):
        tiket = Ticket(self._tiket)
        menu = None
        while menu != 'k':
            if menu == 'e':
                tiket.editTiket()
                pass
            elif menu == 'o':
                tiket.outputTiket()
                pass
            elif menu == 'j':
                tiket.jenisTiket()
                pass
            # elif menu == ''
            menu = menuTiket(menu)

    def output(self, data):
        i = 1
        for x in data:
            print(i, end='. ')
            i += 1
            print(x)
        pass

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                subMenu = input('[D]eparture\n'
                                '[A]rrival\n'
                                '[P]enerbangan\n'
                                '--> ').lower()
                if subMenu == 'p':
                    self.output(self._terbang)
                    pass
                elif subMenu == 'a':
                    self.output(self._arrive)
                    pass
                elif subMenu == 'd':
                    self.output(self._depart)
                    pass
                pass

            elif menu == 'a':
                self.output(self._armada)
                pass
            elif menu == 't':

                pass
            elif menu == 'b':  # buyer
                pass
            elif menu == 'c':  # cuan
                pass
            menu = input('[P]enerbangan\n'
                         '[A]rmada\n'
                         '[T]iket\n'
                         '--> ').lower()

        pass

    pass
