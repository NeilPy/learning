age = "Введите свой возраст: "
age += "\n(Для завершения напишите 'Quit')"


while True:
    message = input(age)

    if message.title() == 'Quit':
        break
    elif int(message) < 3:
        print('Билет бесплатный')
    elif int(message) < 12:
        print('Билет стоит 10$')
    else:
        print('Билет стоит 15$')