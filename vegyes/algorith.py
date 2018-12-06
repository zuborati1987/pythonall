# sorts numbers
# 2018.10.23

numbers = []
i = 0
while 1:
    i += 1
    number = input('Enter numbers %d: '%i)
    if number == '':
        break
    numbers.append(number)
N = len(numbers)
print(numbers)
iterations = 1
while iterations < N:
    j = 0
    while j <= N - 2:
        while numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        j = j + 1
    iterations = iterations + 1 
print (numbers)
