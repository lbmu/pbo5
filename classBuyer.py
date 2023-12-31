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
                    self.pesanTiket()

            elif menu == 'a':
                cari = input('Masukkan kota tujuan\n'
                             '-->')
                if cari in self._arrive:
                    print(f'{cari} Tersedia!')
                    self.pesanTiket()
                
            menu = penerbangan()

    def pesanTiket(self):
        Admin.output(self, self._rute)
        rute = int(input('Pilih Rute:\n--> '))
        print(self._rute[rute-1])
        Admin.output(self, self.tiket.tipeTiket)
        tiket = int(input('Pilih Kelas Tiket:\n--> '))
        print(self.tiket.tipeTiket[tiket-1])
        jumlahTiket = int(input('Pilih Jumlah Tiket:\n--> '))
        print(f'Total Pembayaran\n'
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
            # Milih Tipe Tiket (regular, premium, firstclass)
            # -->
            # Menampilkan jumlah pembayaran
            # -->

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'r':
                self.output(self._rute)
            elif menu == 't':
                self.tiket.outputData()
            elif menu == 'a':
                self.output(self._armada)
            print('[A]rmada | '
                  '[R]ute | '
                  '[T]iket | '
                  '[K]eluar')
            menu = input('--> ').lower()
