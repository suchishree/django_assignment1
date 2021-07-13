for x in range(10):
    print(x)
for x in range(10):
    print(x, end=" ")


print('----------------------------------------------')
# 1 to 100
for x in range(1, 101):
    print(x, end=" ")
print('----------------------------------------------')
# even no from 1 to 10
for x in range(2, 11, 2):
    print(x, end=" ")
print('----------------------------------------------')
# odd no from 1 to 10
for x in range(1, 10, 2):
    print(x, end=' ')
print('----------------------------------------------')
# A TO Z
for x in range(65, 91):
    print(chr(x), end=" ")
print('----------------------------------------------')

# a to z
for x in range(97, 123):
    print(chr(x), end=" ")
print('----------------------------------------------')
# A TO Z and a to z
for x in range(97, 123):
    print(chr(x), " ", chr(x-32))
