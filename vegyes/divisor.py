# greatest common divisor
# 2018.10.23

a = int(input("Give me a number: "))
b = int(input("Give me another number: "))

if a >= b:
    x = int(a/b)
    y = a % b
    while y != 0:
        a = b
        b = y
        x = int(a/b)
        y = a % b
        z = b
else: 
    x = int(b/a)
    y = b % a
    while y != 0:
        b = a
        a = y
        x = int(b/a)
        y = b % a
        z = a
print (z)        