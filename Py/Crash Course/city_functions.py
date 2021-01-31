# 11-1

def get_city_coundtry(city, country, population=''):
    """Форматирует City and Country"""
    if population:
        completely = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        completely = city.title() + ', ' + country.title()
    return completely
