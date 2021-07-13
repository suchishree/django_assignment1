# 6.Write a program input ac no , name, current balance,
# transaction amount, transaction code(d/w) calculate net balance.
account_number = int(input("Enter your account_number"))
Name = input("Enter your name")
money = int(input("enter your amount"))
amount = money % 100
if amount == 0:
    print("your transaction is processing")
    if money <= 10000:
       pin = int(input("enter your pin no"))
       if pin == 1234:
          avl_balance = 30000 - money
          print("your current bal is:",  avl_balance)
       else:
           print("your pin is incorrect")
    else:
        print("your daily limit is 10k")
else:
    print("please enter amount which ends with 00")
