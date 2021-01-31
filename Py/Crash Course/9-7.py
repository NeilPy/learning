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


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['allowed to add messages',
                           'allowed to delete users',
                           'allowed to ban users']

    def show_privileges(self):
        print('---Your privileges---')
        for privileges in self.privileges:
            print(privileges.title())


Steve = Admin('Steve', 'Lower', '23', 'Moscow')
Vilo = Privileges()
Vilo.show_privileges()
Steve.privileges.show_privileges()
