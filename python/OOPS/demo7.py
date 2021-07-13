class Employee:

    def __init__(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print("Employee idno =",self.idno)    
        print("Employee name =",self.name)

emp1 = Employee(101,"ravi") 
emp1.display()


emp2 = Employee(102,"kumar")
emp2.display()