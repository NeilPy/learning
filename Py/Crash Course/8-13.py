def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Kelo', 'Pepio',
                             age='20',
                             location='SPb',
                             number='16')
print(user_profile)
