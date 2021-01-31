import json

from csv_folder.countries import get_country_code

# Список заполняетс данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_date = json.load(f)

# Вывод населения каждой страны за 2010 год.
for pop_dict in pop_date:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)
