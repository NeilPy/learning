def make_sendwichs(*items):
    print('Вы заказали сэндвич со следующими дополнениями: ')
    for item in items:
        print('- ' + item)


make_sendwichs('сыр', 'помидоры', 'зелень')
