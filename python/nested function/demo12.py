def outer():
    print('hey this is rosy')
    a = 100
    print(a)
    def inner():
        print("this is inner")
        a = 43
        b = 7
        return a+b

    res = inner()
    print(res)
outer()