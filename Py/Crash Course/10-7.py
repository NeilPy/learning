while True:
    try:
        print('Для окончания программы напишите q')
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a + b
    except ValueError:
        print("Введено не число")
    else:
        print(int(c))



