# inner function with parameter
def outer():
    print("i am outer")
    a = 1000
    print(a)
    def inner(a,b):
        print("i am inner")
        print(a,b)
    inner("suchishree","badjena")
outer()