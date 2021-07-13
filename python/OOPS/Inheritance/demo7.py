# Hierarchical Inheritance
class A:
    def show_a(self):
        print("i am class A method")
class B(A):
    def show_b(self):
        print("i am class B method")   
class C(A):
    def show_c(self):
        print("i am class C method")  


x = C()
x.show_a()
x.show_c()
print("----------------------------------")

x = B()
x.show_a()
x.show_b()

             