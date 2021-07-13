class Employee:
    comp_name = "sathya"
    comp_cno = 8459003103

    @staticmethod
    def showcompanyinfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)
Employee.showcompanyinfo() #calling static method      