def outer():
    print('hey this is rosy')
    a = 100
    b = 200
    print(a)
    def inner():
        print("this is inner")
        return a+b

    res = inner()
    print(res)
outer()