class Employee:

    def assign(self,idno,name):
        self.idno = idno
        self.name = name
    
class Tempemployee(Employee):
    def assign_salary(self,salary):
        self.salary = salary

    def display(self):
        print("Employee idno =",self.idno)    
        print("Employee name =",self.name)
        print("employee slary=",self.salary)
emp1 = Tempemployee()
emp1.assign(101,"name")
emp1.assign_salary(120000.00)
emp1.display()        
