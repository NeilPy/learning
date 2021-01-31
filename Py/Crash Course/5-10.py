current_users = ['Ae', 'Se', 'De', 'FE', 'Ge']

new_users = ['Ae', 'We', 'Ee', 'Fe', 'GE']

current_user = [current_user.title() for current_user in current_users]

for new_user in new_users:
    if new_user.title() in current_user:
        print("Вы должны выбрать новое имя, это имя: " + new_user + " занято")
    else:
        print("Это имя свободно: " + new_user)
