def make_album(name, name_album, list=''):
    album = {'name': name, 'name_album': name_album}
    if list:
        album['list'] = list
    return album

album1 = make_album('Hendr', 'HeDR')
album2 = make_album('Barre', 'BaRE')
album3 = make_album('Well', 'WL')
album4 = make_album('Dert', 'DT', list=34)
print(album1)
print(album2)
print(album3)
print(album4)
