print("Hello! Welcome to Z-Dictionary")
z_word = input('Enter a word that starts from Z: ').replace('-', '')

z_dict = {'z': 'The 26th and last letter of the english alphabet',
          'zany': 'Strange or unsual in a humorous way',
          'zap': '1. To destroy or kill sb/sth suddenly and with force\n2. To do sth very fast\n3. To use the \x1B[3m' + 'remote control'+ '\x1B[0m' + ' to change television channels quickly',
          'zapper': '1. \x1B[3m' + 'Remote cntrol' + '\x1B[0m' +'\n2. A device or weapon that attacks',
          'zar':'The written abbreviation for South African \x1B[3m' + 'rand' + '\x1B[0m',
          'zeal':'Great energy or enthusiasm connected with sth that you feel strongly about',
          'zealot': 'a person who is extremely enthusiastic about sth, especially religion or politics',
          'zealotry': 'the attitude or behaviour of a zealot',
          'zealous': 'showing great energy and enthusiasm for sth, especially because you feel strongly about it',
          'zebra': 'an African wild animal like a horse with black and white \x1B[3m' + 'stripes' + '\x1B[0m',
          'zebra crossing': 'an area of road marked with broad black and white lines where vehicles must stop for people to walk across'}


while True:
    print(z_dict.get(z_word, 'The word is currently not in our dictionary, please try another word'))
    print('\n')
    z_word = input("Enter another word that starts from 'Z': ")