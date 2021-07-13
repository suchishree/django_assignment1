try:
    no1 = int(input("1st interger  no:"))
    no2 = int(input("2nd integer no:"))
    print("sum=",no1+no2)
    try:
        print("div=",no1/no2)
    except ZeroDivisionError as zde:
        print("can not divide by zero")   
    print("sub=",no1-no2)
    print("mul=",no1*no2)     
except ValueError as ve:
    print("only integer values are allowed")    
print("thanks")
