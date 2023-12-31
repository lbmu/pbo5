# Database = berisi semua keterangan data user, penerbangan, detail tiket, serta data uang user untuk melakukan pembayaran
username = {'admin': 'yoz',
            'manager': ['rusdi'],
            'user': ['jono']}
password = {'admin': '',
            'manager': [''],
            'user': ['']}
data = {'penerbangan': [
    ['jakarta'],  # Departure (dengan syntax data['penerbangan'][0])
    ['bogor']  # Arrival (data['penerbangan'][1])
],
    'rute': ['jakarta - bogor'],
    'armada': ['Rusdi Airline']}

tiket = {'regular': [1000, 0, 800000],  # Jenis Tiket mengikuti key dari dict
         'premium': [700, 0, 1500000],  # List pada index pertama tiket['regular'][0] adalah jumlah tiket
         'firstclass': [198, 2, 2000000]}  # List pada index kedua tiket['regular'][1] adalah Tiket terjual
# List pada index ketiga adalah harga tiket

cuan = {'nama': ['jono'],
        'rute': ['jakarta - bogor'],
        'tiket': ['firstclass'],
        'jumlahTiket': [2],
        'cuan': [40000000]}
# print(type(akun['manajer']))

def typo():
    print('Maaf tidak valid')
