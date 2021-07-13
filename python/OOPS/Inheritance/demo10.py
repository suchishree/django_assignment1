class A:
    def show_a(self):
        print("i am class A method")
class F:
    def show_f(self):
        print("i am class F method")        
class B(A,F):
    def show_b(self):
        print("i am class B method")   
class C(A):
    def show_c(self):
        print("i am class C method")
class D(C):
    def show_d(self):
        print("i am class D method")
class E(C):
    def show_e(self):
        print("i am class E method")



print("-----------------------------------") 
y = B()
y.show_a()
y.show_b()
y.show_f() 
print("----------------------------------")      
z  = D()
z.show_a()
z.show_c()
z.show_d()                        