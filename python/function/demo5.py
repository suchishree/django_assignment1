#Example on function with parameter and with function
def add(no1,no2):
    return no1+no2
def sub(no1,no2):
    print(add(no1,no2))
    return no1-no2
def mul(no1,no2):
    print(sub(no1,no2))
    return no1*no2
def div(no1,no2):
    print(mul(no1,no2))
    return no1/no2
result = div(10,2)
print(result)