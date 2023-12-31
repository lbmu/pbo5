from classManager import *


def inputMenuUser():
    return input('[C]ari | '
                 '[D]aftar | '
                 '[P]esan | '
                 '[K]eluar\n'
                 '--> ').lower()


class Buyer(Manager, Ticket):
    def __init__(self, terbang, armada, rute, tiket, cuan, user):
        Manager.__init__(self, terbang, armada, rute, tiket, cuan)
        # Ticket.__init__(self, tiket)
        self.user = user

    def cariData(self):
        menu = None
        while menu != 'k':
            if menu == 'd':
                cari = input('Masukkan Kota keberangkatan\n'
                             '--> ')
                if cari in self._depart:
                    print(f'{cari} Tersedia!')
                    # Kasih info jika ingin beli Tiket rute ini
                    if input('Apakah anda ingin memesan dengan rute ini?(y/n)\n--> ').lower() == 'y':
                        self.pesanTiket()
                    else:
                        break

            elif menu == 'a':
                cari = input('Masukkan kota tujuan\n'
                             '-->')
                if cari in self._arrive:
                    print(f'{cari} Tersedia!')
                    if input('Apakah anda ingin memesan dengan rute ini?(y/n)\n--> ').lower() == 'y':
                        self.pesanTiket()
                    else:
                        break
                
            menu = penerbangan()

    def pesanTiket(self):
        Admin.output(self, self._rute)
        rute = int(input('Pilih Rute:\n--> '))
        print('Anda memilih rute ', self._rute[rute-1])
        Admin.output(self, self._armada)
        armada = int(input('Pilih armada:\n--> '))
        print(f'Anda memilih armada {self._armada[armada-1]}')
        Admin.output(self, self.tiket.tipeTiket)
        tiket = int(input('Pilih Kelas Tiket:\n--> '))
        print('Anda memilih kelas tiket', self.tiket.tipeTiket[tiket-1], 'dengan harga satu tiket',
              self.tiket.tiket[self.tiket.tipeTiket[tiket-1]][2])
        jumlahTiket = int(input('Pilih Jumlah Tiket:\n--> '))
        print(f'Total Pembayaran\n'
              f'==> Rute : {self._rute[rute-1]}\n'
              f'==> Armada : {self._armada[armada-1]}\n'
              f'==> {jumlahTiket} tiket {self.tiket.tipeTiket[tiket-1]}\n'
              f'==> Anda harus membayar total {jumlahTiket * self.tiket.tiket[self.tiket.tipeTiket[tiket-1]][2]}')
        necromantic = input('Lanjutkan?\n'
                            '(y/n) --> ').lower()
        if necromantic == 'y':
            self.cuan(self.user,
                      self._rute[rute-1],
                      self.tiket.tipeTiket[tiket-1],
                      jumlahTiket)
            print('Tiket berhasil dipesan, silahkan cek aplikasi untuk detail tiket anda')
        else:
            pass

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'r':
                print('===RUTE YANG TERSEDIA===')
                Admin.output(self, self._rute)
            elif menu == 't':
                print('===TIKET YANG TERSEDIA===')
                self.tiket.outputData()
            elif menu == 'a':
                print('===ARMADA YANG TERSEDIA===')
                Admin.output(self, self._armada)
            print('[A]rmada | '
                  '[R]ute | '
                  '[T]iket | '
                  '[K]eluar')
            menu = input('--> ').lower()
