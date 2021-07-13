#parameter
def outer(a):
    print('i am outer')
    print(a)
    def inner():
        print("i am inner")
        print(a)
    inner()
outer("rosy")