a = 1000
print(a)
def outer():
    print('i am outer')
    global a
    a = 30
    print(a)
    def inner():
        print("i am inner")
        print(a)
        a = 46
    inner()
outer()
print(a)