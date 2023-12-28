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
    def __init__(self, terbang, armada, rute, tiket, cuan):
        self._depart = terbang[0]   # Departure
        self._arrive = terbang[1]   # Arrival
        self._rute = rute
        self._armada = armada
        self.tiket = Ticket(tiket)
        self._dataTerbang = len(terbang)
        self._dataArmada = len(armada)
        self.__cuan = cuan
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
                # Kasih jumlah tiket
                # -->
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

    def tiketData(self):
        menu = None
        while menu != 'k':
            if menu == 'e':
                self.tiket.editData()
                pass
            elif menu == 'o':
                self.tiket.outputData()
                pass
            elif menu == 'j':
                self.tiket.jenisTiket()
                pass
            # elif menu == ''
            menu = menuTiket(menu)
        pass

    def cuan(self, siapa, rute, tiket, jml):
        self.__cuan['nama'].append(siapa)
        # self.__cuan['rute'].append(rute)
        # self.__cuan['tiket'].append(tiket)
        # self.__cuan['jumlahTiket'].append(jml)
        cuan = jml * self.tiket.tiket[tiket][1]
        self.tiket.tiket[tiket][0] -= jml
        self.tiket.tiket[tiket][2] += jml
        self.__cuan['cuan'].append(cuan)
        pass

    def __tiketTerjual(self, pilih):
        index = pilih-1
        print('regular =', self.tiket.tiket['regular'][index], 'tiket')
        print('premium =', self.tiket.tiket['premium'][index], 'tiket')
        print('FirstClass =', self.tiket.tiket['firstclass'][index], 'tiket')
        total = (self.tiket.tiket['regular'][index] +
                 self.tiket.tiket['premium'][index] +
                 self.tiket.tiket['firstclass'][index])
        if index == 0:
            print('Total Sisa Tiket = ', total)
        elif index == 1:
            print('Total Terjual = ', total)
        pass



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
                subMenu = int(input('1. Tersisa\n'
                                    '2. Terjual\n'
                                    '--> '))
                self.__tiketTerjual(subMenu)
                # self.tiket.outputData()
                # tampilkan daftar tiket yang terjual
                pass
            elif menu == 'b':  # buyer
                # menampilkan daftar pembeli
                self.output(self.__cuan['nama'])
                '''
                for i in range(len(self.__cuan['nama'])):
                    no = i+1
                    print(f'Data ke-{no}')
                    print(self.__cuan['nama'][i])
                    # print(self.__cuan['rute'][i])
                    # print(self.__cuan['tiket'][i])
                    # print(self.__cuan['jumlahTiket'][i])
                    # print(self.__cuan['cuan'][i])
                    no += 1
                '''
                pass
            elif menu == 'c':  # cuan
                # menampilkan cuan
                for x in self.__cuan['cuan']:
                    print(x, end=' + ')
                totalCuan = sum(self.__cuan['cuan'])
                print('\n==========')
                print(totalCuan)
                pass
            menu = input('[P]enerbangan | '
                         '[A]rmada | '
                         '[T]iket\n'
                         '--> ').lower()

        pass

    pass
