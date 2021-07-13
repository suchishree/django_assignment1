#function with parameter and without return
def add(no1,no2):
    print(no1)
    print(no2)
    print(no1+no2)
add(100,200)
print("------------------------------------")
#lambda function with parameter and without return
x = lambda no1,no2:print("sum",no1+no2)
x(2,3)