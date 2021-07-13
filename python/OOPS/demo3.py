class Employee:

    def assign(self):
        self.idno = 101
        self.name = "ravi"
    def display(self):
        print("Employee idno =",self.idno)    
        print("Employee name =",self.name)

emp1 = Employee() 
emp1.assign()
emp1.display()


emp2 = Employee()
emp2.assign()
emp2.display()



# But instance variable will not hold samevalue that's why the aabove  programm is wrong.
