class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\n' + self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open')

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('WemP', 'Kafe')
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)
