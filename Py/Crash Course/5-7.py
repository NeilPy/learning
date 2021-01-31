favorite_fruits = [fruits for fruits in str(range(1, 50, 5))]
if favorite_fruits in '1':
    print('1 есть в списке')
if favorite_fruits not in '100':
    print('100 нет в списке')
if favorite_fruits in '5':
    print("2 нет в списке")
