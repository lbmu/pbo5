class Admin:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password
        self.jumlahData = len(user)
        # self.key = key
        pass

    def tambahData(self):
        print('===TAMBAH AKUN MANAGER===')
        user = input('username : ')
        password = input('password : ')
        self.__user.append(user)
        self.__password.append(password)
        self.jumlahData += 1
        pass

    def hapusData(self):
        data = input('Masukkan username yang ingin dihapus : ')
        for i in range(self.jumlahData):
            print(i)
            if self.__user[i] == data:
                self.__user.pop(i)
                self.__password.pop(i)
                self.jumlahData -= 1
                break
            pass

    def editData(self):
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

    def outputData(self):
        print('===USER===')
        for x in self.__user:
            print(x)
            pass
        print('===PASSWORD===')
        for x in self.__password:
            print(x)
            pass
        print(self.jumlahData)

    pass
