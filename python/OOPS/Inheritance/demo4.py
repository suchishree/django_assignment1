class A:
    def m1(self):
        print("m1 of class A")
class B:
    def m2(self):
        print("m2 of class B")        
class C(B,A):
    def m3(self):
        print("m3 of class C")
x = C()
x.m1()