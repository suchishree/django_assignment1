#outer function variable can access by inner function
#local variable
def outer():
    print('i am outer')
    a = 100
    print(a)
    def inner():
        print("i am inner")
        print(a)
    inner()
outer()