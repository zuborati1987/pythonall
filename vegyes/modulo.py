# modulo - top 25 3 digit numbers divisible by 7 or 9
# 2018.10.23

numbers = list(range(100, 1000))
n = 1

while n < 26:
    x = max(numbers)
    y = x % 7
    z = x % 9
    if y == 0:
        print(x)
        n += 1
        numbers.pop()
    elif z == 0:
        print(x)
        n += 1
        numbers.pop()
    else:
        numbers.pop()
