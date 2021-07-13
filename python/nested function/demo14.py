def outer():
    print('hey this is rosy')
    def inner():
        print("this is inner")
        a = 43
        b = 7

return a+b
res = outer() #WE CANNOT RETURN OUTSIDE THE FUNCTION
print(res)
