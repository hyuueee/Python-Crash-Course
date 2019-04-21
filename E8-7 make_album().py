def make_album(singer_name, album_name, number_of_songs=''):
    full = {'singer_name': singer_name, 'album_name': album_name}
    if number_of_songs:
        full['number_of_songs'] = number_of_songs
    return full

while True:
    print('\nPlease tell me the singer"s name: ')
    print('(enter"q" at any time to quit')

    singers = input('Singer name:')
    if singers == 'q':
        break
    album = input('album_name:')
    if album == 'q':
        break
print(make_album('singers', 'album'))