# convert numbers to roman numbers
# 2018.10.23

x = input("Give me a number between 1 and 4000: ")
z = int(x)
if z <= 0 or z > 4000:
    print("Wrong input")
    exit()
a = 0
b = 0
c = 0
e = 0
f = 0
g = 0
h = 0

def lenght(x, a, b, c, d):
    a = 0
    b = 0
    c = 0
    e = 0
    if len(x) == 4:
        a = x[-4]
        b = x[-3]
        c = x[-2]
        d = x[-1]

    if len(x) == 3:
        b = x[-3]
        c = x[-2]
        d = x[-1]

    if len(x) == 2:
        c = x[-2]
        d = x[-1]

    if len(x) == 1:
        d = x[-1]
    
    return a, b, c, d

lenght(x, a, b, c, d)

def romans(a, b, c, d, e, f, g, h):
    e = 0
    f = 0
    g = 0
    h = 0
    if d == "1":
        h = "I"
    elif d == "2":
        h = "II"
    elif d == "3":
        h = "III"
    elif d == "4":
        h = "IV"
    elif d == "5":
        h = "V"
    elif d == "6":
        h = "VI"
    elif d == "7":
        h = "VII"
    elif d == "8":
        h = "VIII"
    elif d == "9":
        h = "IX"

    if c == "1":
        g = "X"
    elif c == "2":
        g = "XX"
    elif c == "3":
        g = "XXX"
    elif c == "4":
        g = "XL"
    elif c == "5":
        g = "L"
    elif c == "6":
        g = "LX"
    elif c == "7":
        g = "LXX"
    elif c == "8":
        g = "LXXX"
    elif c == "9":
        g = "XC"

    if b == "1":
        f = "C"
    elif b == "2":
        f = "CC"
    elif b == "3":
        f = "CCC"
    elif b == "4":
        f = "CD"
    elif b == "5":
        f = "D"
    elif b == "6":
        f = "DC"
    elif b == "7":
        f = "DCC"
    elif b == "8":
        f = "DCCC"
    elif b == "9":
        f = "CM"

    if a == "1":
        e = "M"
    elif a == "2":
        e = "MM"
    elif a == "3":
        e = "MMM"
    elif a == "4":
        e = "MV"
    return e, f, g, h

romans(a, b, c, d, e, f, g, h)
solution = e + f + g + h
print (solution)