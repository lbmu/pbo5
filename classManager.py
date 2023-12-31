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
                print(f'Rute {dataDepart} - {dataArrive} berhasil ditambahkan di database')
                # Kasih jumlah tiket
                # -->
            elif menu == 'a':   # Armada
                armada = input('Masukkan Data Armada\n--> ')
                self._armada.append(armada)
                print(f'Armada {armada}')
                self._dataArmada += 1
                print(f'Data armada {armada} berhasil ditambahkan di database')
            menu = inputMenuManager()

    def hapusData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                # Penerbangan
                self.output(self._rute)
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._rute.pop(pivot-1)
                print('Penerbangan berhasil dihapus')
                
            elif menu == 'a':   # Armada
                for i in range(self._dataArmada):
                    print(f'{[i+1]}. {self._armada[i]}')
                pivot = int(input('Masukkan Data yang ingin dihapus = '))
                self._armada.pop(pivot-1)
                print('Armada berhasil dihapus')
            menu = inputMenuManager()

    def editData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':     # Penerbangan
                for i in range(self._dataTerbang):
                    print(f'{i+1}. {self._rute[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._rute[pivot-1] = input('Masukkan data baru\n')
                
            elif menu == 'a':   # Armada
                for i in range(self._dataArmada):
                    print(f'{i+1}. {self._armada[i]}')
                    pivot = int(input('Masukkan Data yang ingin diedit : '))
                    self._armada[pivot-1] = input('Masukkan data armada baru\n')
                
            menu = inputMenuManager()

    def tiketData(self):
        menu = None
        while menu != 'k':
            if menu == 'e':
                self.tiket.editData()
                
            elif menu == 'o':
                self.tiket.outputData()
                
            elif menu == 'j':
                self.tiket.jenisTiket()
                
            # elif menu == ''
            menu = menuTiket(menu)

    def cuan(self, siapa, rute, tiket, jml):
        self.__cuan['nama'].append(siapa)
        # self.__cuan['rute'].append(rute)
        # self.__cuan['tiket'].append(tiket)
        # self.__cuan['jumlahTiket'].append(jml)
        print(self.tiket.tiket[tiket])
        cuan = jml * self.tiket.tiket[tiket][2]
        self.tiket.tiket[tiket][0] -= jml
        self.tiket.tiket[tiket][1] += jml
        self.__cuan['cuan'].append(cuan)

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

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'p':
                print('===DAFTAR RUTE===')
                self.output(self._rute)

            elif menu == 'a':
                print('===DAFTAR ARMADA===')
                self.output(self._armada)
                
            elif menu == 't':
                print('===DAFTAR TIKET===')
                subMenu = int(input('1. Tersisa\n'
                                    '2. Terjual\n'
                                    '--> '))
                self.__tiketTerjual(subMenu)
                # self.tiket.outputData()
                # tampilkan daftar tiket yang terjual
                
            elif menu == 'b':  # buyer
                # menampilkan daftar pembeli
                print('===DAFTAR PEMBELI===')
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
                
            elif menu == 'c':  # cuan
                # menampilkan cuan
                print('===CUAN===')
                for x in self.__cuan['cuan']:
                    print(x, end=' + ')
                totalCuan = sum(self.__cuan['cuan'])
                print('\n==========')
                print(totalCuan)
                
            menu = input('[P]enerbangan | '
                         '[A]rmada | '
                         '[T]iket | '
                         'Pem[b]eli | '
                         '[C]uan | '
                         '[K]eluar'
                         '\n'
                         '--> ').lower()
