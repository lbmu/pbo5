from classAdmin import *
from databasefunction import inputMenu

class Manager(Admin):
    def __init__(self, terbang, armada, tiket):
        super().__init__
        self._terbang = terbang
        self._armada = armada
        self._tiket = tiket
        self._dataTerbang = len(terbang)
        self._dataArmada = len(armada)
        self._dataTiket = len(tiket)
        self.__userQty = None

        pass

    def tambahData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                self._terbang.append(input('Masukkan Data Penerbangan'))
                self._dataTerbang += 1
            elif menu == 'a':
                self._armada.append(input('Masukkan Data Armada'))
                self._dataArmada += 1
                pass
            print('Penambahan Data')
            menu = inputMenu()
        pass

    def hapusData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                for i in range(self._dataTerbang):
                    print(f'{[i+1]}. {self._terbang[i]}')
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._terbang.pop(pivot-1)
                pass
            elif menu == 'a':
                for i in range(self._dataArmada):
                    print(f'{[i+1]}. {self._armada[i]}')
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._armada.pop(pivot-1)
            menu = inputMenu()

        pass

    def editData(self):
        pass

    def tiket(self):
        pass

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                for x in self._terbang:
                    print(x)
                pass
            elif menu == 'a':
                for x in self._armada:
                    print(x)
                pass
            elif menu == 't':
                for x in self._tiket:
                    print(x)
                pass
            elif menu == 'b':  # buyer
                pass
            elif menu == 'c':  # cuan
                pass
            menu = input('')

        pass

    pass
