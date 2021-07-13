class Employee:
    comp_name = "sathya"
    comp_cno = 8459003103

    @staticmethod
    def showcompanyinfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

    def assign(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print("Employee idno =",self.idno)    
        print("Employee name =",self.name)

emp1 = Employee() 
emp1.assign(101,"ravi")
emp1.display()
Employee.showcompanyinfo()


emp2 = Employee()
emp2.assign(102,"kumar")
emp2.display()  
Employee.showcompanyinfo()  
