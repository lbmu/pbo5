import abc


class Admin:
    def __init__(self, user, pwd):
        self.__user = user              # daftar username manager
        self.__password = pwd           # daftar password manager
        self.__jumlahData = len(user)   # jumlah manager
        # self.key = key
        pass

    @property
    def panggilUser(self):
        return self.__user

    # @abc.abstractmethod
    # def kosong(self):
    #     pass

    def tambahData(self):
        print('===TAMBAH AKUN MANAGER===')
        print('USERNAME YANG TERSEDIA : ')
        self.output(self.__user)
        user = input('username : ')
        password = input('password : ')
        self.__user.append(user)
        self.__password.append(password)
        self.__jumlahData += 1
        pass

    def hapusData(self):
        print('===HAPUS USERNAME===')
        self.output(self.__user)
        data = input('Masukkan username yang ingin dihapus : ')
        for i in range(self.__jumlahData):
            print(i)
            if self.__user[i] == data:
                self.__user.pop(i)
                self.__password.pop(i)
                self.__jumlahData -= 1
                break
            pass

    def editData(self):
        self.output(self.__user)
        data = input('Masukkan username yang ingin diedit : ')
        for i in range(self.__jumlahData):
            if self.__user[i] == data:
                menu = None
                while menu != 'k':
                    if menu == 'u':
                        self.__user[i] = input('username baru : ')
                        pass
                    elif menu == 'p':
                        self.__password[i] = input('password baru : ')
                        pass
                    menu = input('[U]sername | '
                                 '[P]assword | '
                                 '[K]eluar\n'
                                 '--> ').lower()
                pass
        pass

    def output(self, data):
        i = 1
        for x in data:
            print(f'({i}) {x}')
            i += 1
        pass

    def outputData(self):
        print('===USER===')
        self.output(self.__user)
        print('===PASSWORD===')
        self.output(self.__password)
        print('===JUMLAH MANAGER===')
        print(self.__jumlahData, 'Manager')

    pass
