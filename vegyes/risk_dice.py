# risk dice roll calculator
# 2018.10.22

from random import randint


def result():
    print(randint(1, 6))


x = int(input("How many attacker dice? "))
y = int(input("How many defender dice? "))
print("Attacker results: ")
if x == 3:
    result()
    result()
    result()
elif x == 2:
    result()
    result()
elif x == 1:
    result()

print("Defender results: ")
if y == 2:
    result()
    result()
else:
    result()
