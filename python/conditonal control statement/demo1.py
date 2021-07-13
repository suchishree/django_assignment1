#ATM withdraw operation
pin = int(input("enter your pin"))
if pin == 1234:
    print("your pin is correct")
    money = int(input("enter your amount"))
    amount = money % 100
    if money >= 30000:
            print("you don't have sufficient balance")
    elif amount == 0:
        print("pls wait your transaction is processing")
        avl_balance = 30000 - money
        print("avl balance:",avl_balance)
        print("your transcation is successful")
        if money > 10000:
            print("pls enter amount less than 10000")
    else:
        print("please enter the amount which ends with 00")

else:
    print("your pin is incorrect")
