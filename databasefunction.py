username = {'admin': 'yoz',
            'manager': [''],
            'user': ['']}
password = {'admin': '',
            'manager': [''],
            'user': ['']}
data = {'penerbangan': [
    ['jakarta'],     # Departure (dengan syntax data['penerbangan'][0])
    ['bogor']      # Arrival (data['penerbangan'][1])
],
    'rute': ['jakarta - bogor'],
    'armada': ['Rusdi Airline']}

tiket = {'regular':    [1000, 800000],     # Jenis Tiket mengikuti key dari dict
         'premium':    [700, 1500000],     # List pada index pertama (0) adalah jumlah tiket
         'firstclass': [200, 2000000]}     # List pada index kedua (10, 20, 30) adalah Harga Tiket


# print(type(akun['manajer']))
