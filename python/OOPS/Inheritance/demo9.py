#HYBRID INHITANCE
class A:
    def show_a(self):
        print("i am class A method")
class B(A):
    def show_b(self):
        print("i am class B method")   
class C(A):
    def show_c(self):
        print("i am class C method")
class D(B,C):
    def show_d(self):
        print("i am class D method")
x = D()
x.show_a()
x.show_b()
x.show_c()
x.show_d()              