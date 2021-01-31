from User import User

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