a = 1000
def outer():
    print('i am outer')
    global a
    a = 30
    print(a)
    def inner():
        print("i am inner")
        print(a)
    inner()
outer()
print(a)