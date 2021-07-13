class Employee:
    def __init__(self):
        print("Employee class")
        self.idno = 101
class Tempemployee(Employee):
    def display(self):
        print("Employee idno = ",self.idno)
emp1 = Tempemployee()
emp1.display()                