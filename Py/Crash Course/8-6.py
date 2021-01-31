def city_country(city, country):
    format_cc = city.title() + ', ' + country.title()
    return format_cc

cityCountry1 = city_country('Москва', 'Россия')
cityCountry2 = city_country('СПб', 'Россия')
cityCountry3 = city_country('Киев', 'Украина')

print(cityCountry1)
print(cityCountry2)
print(cityCountry3)