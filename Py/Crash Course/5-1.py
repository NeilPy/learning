numbers = [number for number in range(1, 20)]
name = ['AWE', 'Awe', 'fel', 'FEL']
print(numbers)
print("1 in Numbers == True")
print(1 in numbers)
print("22 in Numbers == False")
print(22 in numbers)
print("4 in Numbers == True")
print(4 in numbers)
print("50 in Numbers == False")
print(50 in numbers)
if 120 not in numbers:
    print("True == 120")
if 100 not in numbers:
    print("True == 100")
if 10 not in numbers:
    print("True == 10")
else:
    print("False == 10")
if 22 not in numbers:
    print("True == 22")
if 10 in numbers:
    print("True == 10")
if 22 in numbers:
    print("True == 22")
else:
    print("False == 22")
