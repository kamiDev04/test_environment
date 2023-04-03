def make_album(artist, album, tracks = None):
    if tracks:
        album_name = {'artist': artist, 'album': album, 'tracks': tracks}
    else:
        album_name = {'artist': artist, 'album': album}
    return album_name

while True:
    print('\nPlease input artist:')
    print('(enter "q" at any time to quit')

    artist_input = input('Artist: ')
    if artist_input == 'q':
        break

    album_input = input('Album: ')
    if album_input == 'q':
        break

    fin_album = make_album(artist_input, album_input)
    print(fin_album)

