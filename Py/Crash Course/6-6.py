favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
passed = ['jen', 'edward', 'Elas']

for name in favorite_languages.keys():
    if name in passed:
        print('Спасибо, ' + name.title() + " за прохождение опроса")
    else:
        print('Хотите пройти тест ' + name.title())
