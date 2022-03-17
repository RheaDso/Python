class Person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    def __str__(self):
        return self.firstname+""+self.lastname
class Employee(Person):
    def __init__(self, first, last, staffnumber):
        super().__init__(first, last)
        self.staffnumber=staffnumber

x=Person("Marge", "Simpson")
y=Employee("Homer", "Simpson", "100")
print(x)
print(y)                

