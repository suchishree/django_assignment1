# 5. Print sum of  prime numbers between 1 to 100
sum = 0
for x in range(1, 101):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
               break
        else:
            print(x, "is a prime number")
            sum = sum + x

print("The of prime numbers:",sum)



