class Employee:

    def assign(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print("Employee idno =",self.idno)    
        print("Employee name =",self.name)

emp1 = Employee() 
emp1.assign(101,"ravi")
emp1.display()


emp2 = Employee()
emp2.assign(102,"kumar")
emp2.display()