def increment(number):
    number = number+1
    return number
def decrement(number):
    number = number-1
    return number
def operation(function_name,no):
    result = function_name(no)
    print(result)
operation(increment,100)
operation(decrement,1000)