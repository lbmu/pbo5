class Admin:
    def __init__(self, user, pwd):
        self.__user = user              # daftar username manager
        self.__password = pwd           # daftar password manager
        self.__jumlahData = len(user)   # jumlah manager
        # self.key = key

    @property
    def panggilUser(self):
        return self.__user

    # @abc.abstractmethod
    # def kosong(self):
    #     

    def tambahData(self):
        print('===TAMBAH AKUN MANAGER===')
        print('USERNAME YANG TERSEDIA : ')
        self.output(self.__user)
        user = input('username : ')
        password = input('password : ')
        self.__user.append(user)
        self.__password.append(password)
        self.__jumlahData += 1
        print(f"Username {user} berhasil ditambahkan ")

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
                print(f"Username {data} berhasil dihapus ")
                break

    def editData(self):
        self.output(self.__user)
        data = input('Masukkan username yang ingin diedit : ')
        for i in range(self.__jumlahData):
            if self.__user[i] == data:
                menu = None
                while menu != 'k':
                    if menu == 'u':
                        self.__user[i] = input('username baru : ')

                    elif menu == 'p':
                        self.__password[i] = input('password baru : ')
                    print(f"Usern {data} berhasil diubah ")

                    menu = input('[U]sername | '
                                 '[P]asspassword | '
                                 '[K]eluar\n'
                                 '--> ').lower()

    def output(self, data):
        i = 1
        for x in data:
            print(f'({i}) {x}')
            i += 1

    def outputData(self):
        print('===USER===')
        self.output(self.__user)
        print('===PASSWORD===')
        self.output(self.__password)
        print('===JUMLAH MANAGER===')
        print(self.__jumlahData, 'Manager')
