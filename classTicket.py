
def menuTiket(menu):
    while menu != 'i':
        menu = input('[E]dit\n'
                     '[O]utput\n'
                     '[K]embali\n'
                     '--> '
                     )
        return menu
        pass
    pass


class Ticket:
    def __init__(self, tiket):
        self.__tiket = tiket
        self.__jenisTiket = []
        for x in self.__tiket:
            self.__jenisTiket.append(x)
        pass

    @property
    def tiket(self):
        return self.__tiket

    def inputTiket(self, ubah, jenis):
        if ubah == 'j':
            self.__tiket[self.__jenisTiket[jenis]][0] = int(input('Jumlah Baru\n--> '))
            pass
        elif ubah == 'h':
            self.__tiket[self.__jenisTiket[jenis]][1] = int(input('Harga Baru\n--> '))
            pass


    def jenisTiket(self):
        key = self.__tiket.keys()
        i = 1
        for x in key:
            print(f'{i}. {x}')
            i += 1
            pass
        pass

    def editTiket(self):
        menu = None
        while menu != 'k':
            if menu == 'j':
                self.jenisTiket()
                pivot = int(input('Tiket Tipe : '))
                index = pivot - 1
                if pivot == 1:
                    self.inputTiket(menu, index)
                    pass
                elif pivot == 2:
                    self.inputTiket(menu, index)
                    pass
                elif pivot == 3:
                    self.inputTiket(menu, index)
                    pass
                pass
            elif menu == 'h':
                self.jenisTiket()
                pivot = int(input('Tiket Tipe : '))
                index = pivot - 1
                if pivot == 1:
                    self.inputTiket(menu, index)
                    pass
                elif pivot == 2:
                    self.inputTiket(menu, index)
                    pass
                elif pivot == 3:
                    self.inputTiket(menu, index)
                    pass
                pass
            menu = input('[J]umlah\n'
                         '[H]arga\n'
                         '[K]eluar\n'
                         '--> ')

        pass

    def output(self, index):
        print(self.__jenisTiket[index])
        print(f'Sisa : {self.__tiket[self.__jenisTiket[index]][0]}\n'
              f'Harga : {self.__tiket[self.__jenisTiket[index]][1]}')
        pass

    def outputTiket(self):
        menu, index = None, None
        while menu != 4:
            if menu == 1:
                self.output(index)
                pass
            elif menu == 2:
                self.output(index)
                pass
            elif menu == 3:
                self.output(index)
                pass
            self.jenisTiket()
            print('4. Keluar')
            menu = int(input(''))
            index = menu - 1

    pass
