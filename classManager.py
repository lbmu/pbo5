from classTicket import *


def penerbangan():
    return input('[D]eparture | '
                 '[A]rrival | '
                 '[K]eluar\n'
                 '--> ').lower()


def inputMenuManager():
    return input('======\n'
                 '[P]enerbangan | '
                 '[A]rmada | '
                 '[K]eluar\n'
                 '--> ').lower()


class Manager(Admin):
    def __init__(self, terbang, armada, rute, tiket):
        self._depart = terbang[0]   # Departure
        self._arrive = terbang[1]   # Arrival
        self._rute = rute
        self._armada = armada
        self.tiket = Ticket(tiket)
        self._dataTerbang = len(terbang)
        self._dataArmada = len(armada)
        self.__userQty = None
        pass

    def tambahData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                dataDepart = input('Departure : ')
                self._depart.append(dataDepart)
                dataArrive = input('Tujuan : ')
                self._arrive.append(dataArrive)

                self._rute.append(f'{dataDepart} - {dataArrive}')
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
                self.output(self._rute)
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._rute.pop(pivot-1)
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
                    print(f'{i+1}. {self._rute[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._rute[pivot-1] = input('Masukkan data baru\n')
                pass
            elif menu == 'a':   # Armada
                for i in range(self._dataArmada):
                    print(f'{i+1}. {self._armada[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._armada[pivot-1] = input('Masukkan data baru\n')
                pass
            menu = inputMenuManager()
        pass

    def tiketData(self, tiket):
        self.tiket = tiket
        tiket = Ticket(self.tiket)
        menu = None
        while menu != 'k':
            if menu == 'e':
                tiket.editData()
                pass
            elif menu == 'o':
                tiket.outputData()
                pass
            elif menu == 'j':
                tiket.jenisTiket()
                pass
            # elif menu == ''
            menu = menuTiket(menu)

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                subMenu = None
                while subMenu != 'k':
                    if subMenu == 'p':
                        self.output(self._rute)
                        pass
                    elif subMenu == 'a':
                        self.output(self._arrive)
                        pass
                    elif subMenu == 'd':
                        self.output(self._depart)
                        pass
                    subMenu = input('[D]eparture | '
                                    '[A]rrival | '
                                    '[P]enerbangan | '
                                    '[K]eluar\n'
                                    '--> ').lower()
                pass

            elif menu == 'a':
                self.output(self._armada)
                pass
            elif menu == 't':
                self.tiket.outputData()
                pass
            elif menu == 'b':  # buyer
                pass
            elif menu == 'c':  # cuan
                pass
            menu = input('[P]enerbangan | '
                         '[A]rmada | '
                         '[T]iket\n'
                         '--> ').lower()

        pass

    pass
