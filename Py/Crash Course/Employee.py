# 11-3

class Employee:
    """Класс представляющий работника."""

    def __init__(self, first_name, last_name, annual_salary=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        self.annual_salary += self.annual_salary + ' $'
        return self.annual_salary


Joe = Employee('Joe', 'Loep', '')
print(Joe.give_raise())

