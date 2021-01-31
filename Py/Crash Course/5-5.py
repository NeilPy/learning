alien_color = str(input('Выберите цвет: green, yellow, red: '))
if alien_color.lower() == 'green':
    print('Вы получили 5 очков')
elif alien_color.lower() == 'yellow':
    print('Вы получили 10 очков')
else:
    print('Вы получили 15 очков')