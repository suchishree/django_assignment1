def outer():
    print("i am outer")
    def inner():
        print("i am inner")
    return inner
x = outer()
x()