class Admin:
    def __init__(self, user, pwd):
        self.__user = user  # daftar username manager
        self.__password = pwd   # daftar password manager
        self.jumlahData = len(user) # jumlah manager
        # self.key = key
        pass

    def _tambahData(self):
        print('===TAMBAH AKUN MANAGER===')
        user = input('username : ')
        password = input('password : ')
        self.__user.append(user)
        self.__password.append(password)
        self.jumlahData += 1
        pass

    def _hapusData(self):
        data = input('Masukkan username yang ingin dihapus : ')
        for i in range(self.jumlahData):
            print(i)
            if self.__user[i] == data:
                self.__user.pop(i)
                self.__password.pop(i)
                self.jumlahData -= 1
                break
            pass

    def _editData(self):
        data = input('Masukkan username yang ingin diedit : ')
        for i in range(self.jumlahData):
            if self.__user[i] == data:
                menu = None
                while menu != 'k':
                    if menu == 'u':
                        self.__user[i] = input('username baru : ')
                        pass
                    elif menu == 'p':
                        self.__password[i] = input('password baru : ')
                        pass
                    menu = input('[U]sername\n'
                                 '[P]assword\n'
                                 '[K]eluar\n').lower()
                pass
        pass

    def output(self, data):
        i = 1
        for x in data:
            print(i, end='. ')
            i += 1
            print(x)
        pass

    def outputData(self):
        print('===USER===')
        self.output(self.__user)
        print('===PASSWORD===')
        self.output(self.__password)
        print(self.jumlahData)

    pass
