file_name = 'guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        name = input('(Введите q для выхода)'
                     '\nВведите свое имя: ')
        print('Здравствуйте, ' + name.title() + '.')
        if name == 'q':
            break
        else:
            file_object.write('Здравствуйте, ' + name.title() + '.\n')
