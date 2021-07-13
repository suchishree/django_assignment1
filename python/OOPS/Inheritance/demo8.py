# Hierarchical Inheritance
class A:
    def __init__(self):
        super().__init__()
        print("i am class A const")
class B(A):
    def __init__(self):
        super().__init__()
        print("i am class B const")   
class C(A):
    def __init__(self):
        super().__init__()
        print("i am class C const")
x = C()


print("------------------------")


x = B()

