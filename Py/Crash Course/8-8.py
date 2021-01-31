def make_album(name, name_album, list_album=''):
    album = {'name': name, 'name_album': name_album}
    if list_album:
        album['list'] = list_album
    return album


while True:
    print('\nНапишите имя исполнителя')
    print('(Напишите q чтобы закончить создания альбомов)')

    p_name = input('Название исполнителя: ')
    if p_name == 'q':
        break

    alb_name = input('Название альбома: ')
    if alb_name == 'q':
        break

    format_album = make_album(p_name, alb_name)
    print(format_album)
