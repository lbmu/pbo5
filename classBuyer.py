from classManager import *
from classTicket import Ticket
from databasefunction import penerbangan, tiket


class Buyer(Manager, Ticket):
    def __init__(self, terbang, armada):
        Manager.__init__(self, terbang, armada)
        Ticket.__init__(self, tiket)
        self.terbang = terbang
        # self.tiket =
        # super().__init__
        pass

    def cariData(self):
        menu = None
        while menu != 'k':
            if menu == 'd':
                cari = input('Masukkan Kota keberangkatan\n'
                             '--> ')
                pass
            elif menu == 'a':
                pass
            menu = penerbangan()
        pass

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'd':
                self.output(self._terbang)
            elif menu == 't':
                self.output(self.tiket)
            elif menu == 'a':
                self.output(self._armada)

            menu = input()

    pass
