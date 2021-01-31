class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = age
        self.location = location

    def describ_user(self):
        print("\nUser info: " + self.full_name.title() +
              ' age: ' + str(self.age) + ' location: ' +
              self.location.title())

    def greet_user(self):
        print('Hello ' + self.full_name.title() + ' !')


John = User('John', 'Lomest', '21', 'NY')
John.describ_user()
John.greet_user()


Jim = User('Jim', 'Worter', '23', 'Boston')
Jim.describ_user()
Jim.greet_user()
