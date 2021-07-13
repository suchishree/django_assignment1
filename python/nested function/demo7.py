a = 1000
print(a)
def outer():
    print('i am outer')
    global a
    a = 30
    print(a)
    def inner():
        print("i am inner")
        global a
        a = 45
        print(a)
    inner()
outer()
print(a)