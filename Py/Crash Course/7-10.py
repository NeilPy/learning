responses = {}

active = True

while active:
    name = input('Введите свое имя: ')
    response = input('Где бы вы хотели отдохнуть: ')

    responses[name] = response

    repeat = input('Хотите продолжить опрос? (yes/no) ')
    if repeat == 'no':
        active = False

print('\n--- Все прошедние опрос ---')
for name, response in responses.items():
    print(name + ' хочет одхонуть ' + response + '.')


