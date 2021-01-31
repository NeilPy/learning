file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    file_object.write((input('Введите свое имя: ')))