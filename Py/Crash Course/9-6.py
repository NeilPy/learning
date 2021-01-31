class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('\n' + self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['AppleJu', 'MorsLe', 'LemonePie']

    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor)


IceCream = IceCreamStand('IceStand', 'Stand')
IceCream.open_restaurant()
IceCream.describe_flavors()
