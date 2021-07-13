class A:
    def __init__(self):
        super().__init__()
        print("A class const")
class B:
    def __init__(self):
        
        print("B class const")        
class C(A,B):
    def show(self):
        print("C class method")
x = C()
x.show() 