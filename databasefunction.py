username = {'admin': 'yoz',
            'manager': [''],
            'user': ['']}
password = {'admin': '',
            'manager': [''],
            'user': ['']}
data = {'penerbangan': [
    ['Jakarta'],     # Departure (dengan syntax data['penerbangan'][0])
    ['Surabaya']      # Arrival (data['penerbangan'][1])
],
    'armada': ['Rusdi Airline']}

tiket = {'regular':    [1000, 800000],     # Jenis Tiket mengikuti key dari dict
         'premium':    [700, 1500000],     # List pada index pertama (0) adalah jumlah tiket
         'firstclass': [200, 2000000]}     # List pada index kedua (10, 20, 30) adalah Harga Tiket


# print(type(akun['manajer']))
def inputMenuPriv():
    return input("[T]ambah\n"
                 "[H]apus\n"
                 "[E]dit\n"
                 "[O]utput\n"
                 "[L]ainnya\n"
                 "[K]eluar\n").lower()
    pass


def inputMenuManager():
    return input('======\n'
                 '[P]enerbangan\n'
                 '[A]rmada\n'
                 '[K]eluar\n').lower()


def inputMenuUser():
    return input('[C]ari\n'
                 '[D]aftar\n'
                 '[P]esan\n'
                 '--> ').lower()


def penerbangan():
    return input('[D]eparture\n'
                 '[A]rrival\n'
                 '[K]eluar\n'
                 '--> ').lower()
