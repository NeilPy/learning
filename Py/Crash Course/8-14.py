def make_car(model_car, name_car, **car_info):
    cars = {'model_car': model_car, 'name_car': name_car}
    for key, value in car_info.items():
        cars[key] = value
    return cars


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
