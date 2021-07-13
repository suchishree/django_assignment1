a = 1000
def outer():
    print('i am outer')
    print(a)
    def inner():
        print("i am inner")
        print(a)
    inner()
outer()