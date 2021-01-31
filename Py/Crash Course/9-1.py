class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('\n' + self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open')


restaurant = Restaurant('WemP', 'Kafe')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('Lemo', 'Top')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant('Mool', 'Best')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()