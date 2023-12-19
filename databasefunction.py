

username = {'admin': 'yoz',
            'manager': [''],
            'user': ['shinji']}
password = {'admin': '',
            'manager': [''],
            'user': ['ta']}
data = {'penerbangan': [],
        'armada': []}

tiket = {'regular': 0,
         'premium': 1,
         'firstclass': 2}


# print(type(akun['manajer']))
def inputMenuPriv():
    return input("[T]ambah\n"
                 "[H]apus\n"
                 "[E]dit\n"
                 "[O]utput\n"
                 "[K]eluar\n").lower()
    pass


def inputMenu():
    return input('======\n'
                 'Penerbangan\n'
                 'Armada\n'
                 'Keluar\n').lower()
