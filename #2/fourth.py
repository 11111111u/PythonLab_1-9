class Person:
    def print_info(self):
        print(self.name,'is',self.age)

alex=Person();
alex.name='Alex';
alex.age=18
john = Person();
john.name = 'John';
john.age = 20

print(type(Person.print_info))

Person.print_info(alex)
Person.print_info(john)
print(type(alex.print_info))
alex.print_info()
john.print_info()
