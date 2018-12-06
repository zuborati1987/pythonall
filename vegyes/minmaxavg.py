# calculate with restrictions
# 2018.10.24

x = 0
y = 1

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

while x < 7:
    if numbers[x] < numbers[y]:
        min = numbers[x]
        max = numbers[y]
        x += 1
        y += 1
    else:
        min = numbers[y]
        max = numbers[x]
        x += 1
        y += 1

print(min, max)

sum = 0
avg = 0
x = 0
while x < len(numbers):
    sum = sum + numbers[x]
    x += 1

avg = sum/len(numbers)

print(avg)
