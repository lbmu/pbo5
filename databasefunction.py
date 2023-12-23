username = {'admin': 'yoz',
            'manager': ['', 'rusdi'],
            'user': ['']}
password = {'admin': '',
            'manager': [''],
            'user': ['']}
data = {'penerbangan': [
    ['jakarta'],        # Departure (dengan syntax data['penerbangan'][0])
    ['bogor']           # Arrival (data['penerbangan'][1])
],
    'rute': ['jakarta - bogor'],
    'armada': ['Rusdi Airline']}

tiket = {'regular':    [1000, 800000],     # Jenis Tiket mengikuti key dari dict
         'premium':    [700, 1500000],     # List pada index pertama tiket['regular'][0] adalah jumlah tiket
         'firstclass': [200, 2000000]}     # List pada index kedua tiket['regular'][1] adalah Harga Tiket

# print(type(akun['manajer']))
