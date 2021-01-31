import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
def get_stored_username():
    """"Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    """Запрашивает новое имя пользователя."""
    username = input("Как тебя зовут ? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def great_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print('С возвращением, ' + username.title() + '!')
    else:
        username = get_new_user()
        print('Мы вас запомним возвращайтесь снова, '
              + username + '!')


great_user()
