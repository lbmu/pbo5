from databasefunction import typo
class Admin:
    def __init__(self, user, pwd):
        self.__user = user              # daftar username manager
        self.__password = pwd           # daftar password manager
        self.__jumlahData = len(user)   # jumlah manager

    # Method untuk admin menambah data akun user
    def tambahData(self): 
        print('===TAMBAH AKUN MANAGER===')
        print('USERNAME YANG TERSEDIA : ')
        self.output(self.__user)
        user = input('username : ')
        password = input('password : ')
        self.__user.append(user)
        self.__password.append(password)
        self.__jumlahData += 1
        self.konfirmasi('t', user)
        
    # Method untuk admin menghapus data akun yang sudah terdaftar di "databasefunction.py"
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
                self.konfirmasi('h', data)
                break
                
    # Method untuk admin mengubah data akun yang sudah terdaftar di "databasefunction.py"
    def editData(self):
        self.output(self.__user)
        data = input('Masukkan username yang ingin diedit : ')
        for i in range(self.__jumlahData):
            if self.__user[i] == data:
                menu = None
                while menu != 'k':
                    if menu == 'u':
                        self.__user[i] = input('username baru : ')
                        self.konfirmasi('u', self.__user)
                        
                    elif menu == 'p':
                        self.__password[i] = input('password baru : ')
                        self.konfirmasi('p', self.__password)

                    else :
                        pass
                    

                    menu = input('[U]sername | '
                                 '[P]assword | '
                                 '[K]eluar\n'
                                 '--> ').lower()
                    
    # Method statik untuk membantu program lain dalam melakukan output
    def output(self, data):
        i = 1
        for x in data:
            print(f'({i}) {x}')
            i += 1

    def konfirmasi(self, menu, data):
        if menu == 't':
            print(f'Data {data} berhasil ditambahkan')
        elif menu == 'h':
            print(f'Data {data} berhasil dihapus')
        elif menu == 'e':
            print(f'Data {data} berhasil diubah')
        elif menu == 'p' :
            print(f'Password telah diganti di database menjadi {data}')
        elif menu == 'u' :
            print(f'Username telah diganti di database menjadi {data}')
    # Method yang dilakukan admin untuk meanampilkan data akun yang tersedia di "databasefunction.py"
    def outputData(self):
        print('===USER===')
        self.output(self.__user)
        print('===PASSWORD===')
        self.output(self.__password)
        print('===JUMLAH MANAGER===')
        print(self.__jumlahData, 'Manager')
