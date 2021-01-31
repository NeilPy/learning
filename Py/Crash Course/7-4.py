pizza = "Введите дополнение к пицце:"
pizza += "\n(Введите 'Quit' для завершения.)"

active = True
while active:
    message = input(pizza.title())

    if message == 'Quit':
        active = False
    else:
        print("Дополнение к пицце добавлено: " + message)
