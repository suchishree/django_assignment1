def outer():
    print('hey this is rosy')
    a = 100
    print(a)
    def inner():
        print("this is inner")
        a = 43
        print(a)
    inner()
    print(a)
outer()