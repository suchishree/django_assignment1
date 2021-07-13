class A:
    def __init__(self):
        print("A class const")
class B:
    def __init__(self):
        super().__init__()
        print("B class const")        
class C(B,A):
    def show(self):
        print("C class method")
x = C()
x.show()        