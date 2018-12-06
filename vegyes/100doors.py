# goes around opening and closing doors
# 2018.10.25

doors = (list(range(1, 101)))


def doors_oc():
    x = 0
    while x < 100:
        doors[x] = str(doors[x]) + " open"
        x += 1


doors_oc()

step_size = 2
y = 2


while step_size < len(doors):
    while y < len(doors):
        if " closed" in doors[y-1]:
            doors[y-1] = doors[y-1].replace(" closed", " open")
            y += step_size
        elif " open" in doors[y-1]:
            doors[y-1] = doors[y-1].replace(" open", " closed")
            y += step_size
    step_size += 1
    y = step_size

for d in doors:
    if " open" in d:
        print(d)






# while y < 100:
# for i in range(0, len(doors), 2):
    # for d in doors:
        # d.replace(' closed', ' open') 
# doors = [d.replace(' open', ' closed') for d in doors]
