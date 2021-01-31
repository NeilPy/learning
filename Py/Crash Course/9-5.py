class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describ_user(self):
        print("\nUser info: " + self.full_name.title() +
              ' age: ' + str(self.age) + ' location: ' +
              self.location.title())

    def greet_user(self):
        print('Hello ' + self.full_name.title() + ' !')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


John = User('John', 'Lomest', '21', 'NY')
John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()
print(John.login_attempts)
John.reset_login_attempts()
print(John.login_attempts)