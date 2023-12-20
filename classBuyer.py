from classManager import *
from classTicket import Ticket
from databasefunction import penerbangan


class Buyer(Manager, Ticket):
    def __init__(self, terbang, armada, tiket):
        # super().__init__
        Manager.__init__(self, terbang, armada, tiket)
        self.terbang = terbang
        self.armada = armada
        self.tiket = tiket

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
            print(self.terbang)
            menu = input()

    pass
