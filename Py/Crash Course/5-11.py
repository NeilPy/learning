numbers = [number for number in range(1, 10)]

for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')

# 5-11. Порядковые числительные: порядковые числительные в английском языке заканчиваются суффиксом th
# (кроме 1st, 2nd и 3rd).
# Сохраните числа от 1 до 9 в списке.
# Переберите элементы списка.
# Используйте цепочку if-elif-else в цикле для вывода правильного окончания числительного для каждого числа.
# Программа должна выводить числительные «1st 2nd 3rd 4th 5th 6th 7th 8th 9th»,
# причем каждый результат должен располагаться в отдельной строке.
