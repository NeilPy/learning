numbers = {
    'Le': [1, 2, 4, 6],
    'Be': [5, 2, 0, 10],
    'Er': [2, 6, 12, 55],
    'We': [66, 53, 21],
    'By': [16, 177, 34, 60],
    }

for name, numbers in numbers.items():
    print("\n" + name.title() + " favorite numbers: ")
    for number in numbers:
        print("\t" + str(number))