from collections import OrderedDict

glossary = {}
glossary['ident'] = 'идентификатор'
glossary['ip'] = 'уникальный адрес компьютера в сети Интернет. Этот адрес каждому компьютеру присваивает провайдер,'
glossary['bug'] = 'ошибка в программе/коде, из-за которой результаты выполнения программы неправильные.'
glossary['link'] = 'ссылка на какой-либо ресурс.'

print(glossary)

for word, info in glossary.items():
    print(word.title() + ": " + info + ". \n")
