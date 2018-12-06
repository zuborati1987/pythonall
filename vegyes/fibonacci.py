# print out the first 30 fibonacci numbers
# 2018.10.22

n = 1
a = 1
b = 1
while n <= 30:
    print(a+b)
    x = a
    y = b
    a = y
    b = x + y
    n += 1
