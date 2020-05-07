
class Employee:
    def __init__(self, first_name, last_name):
        self.full_name = first_name + " " + last_name
        print("Employee: {}".format(self.full_name))
        self.email = first_name + "." + last_name
        print("Email: {}@company.net".format(self.email.lower()))



zainab = Employee("z","ali")
print(zainab.full_name)