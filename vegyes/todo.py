# lists tasks to do
# 2018.10.25

num_lines = 0
with open("todo.txt", 'r') as f:
    for line in f:
        num_lines += 1
f.close()

if num_lines == 0:
    numbering = 1
else:
    numbering = num_lines


def remove_numbering():
    f = open("todo.txt")
    lines = f.readlines()
    f.close()
    f = open("todo.txt", 'w')
    for line in lines:
        f.write(line[1:])
    f.close()


def give_newnumber():
    with open('todo.txt', 'r') as program:
        data = program.readlines()

    with open('todo.txt', 'w') as program:
        for (number, line) in enumerate(data):
            program.write('%d%s' % (number+1, line))
    f.close()


user_input = input("Please specify a command [list, add, mark, archive]: ")

if user_input == "list":
    f = open("todo.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)
    f.close()

elif user_input == "add":
    f = open("todo.txt", "a+")
    f.write("{}.[ ]" .format(numbering))
    f.write(input())
    f.write("\n")
    f.close()
    num_lines = 0

elif user_input == "mark":
    f = open("todo.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)
    for_mark = int(input("Which line would you like to mark? "))
    f.close()

    with open('todo.txt', 'r') as file:
        data = file.readlines()
        data[for_mark] = data[for_mark].replace("[ ]", "[x]")
    with open('todo.txt', 'w') as file:
        file.writelines(data)
    f.close()

    f = open("todo.txt", "r")
    f1 = f.readlines()
    for x in f1:
        print(x)
    f.close()


elif user_input == "archive":
    to_archive = ["[x]"]
    with open('todo.txt') as oldfile, open('todoreplace.txt', 'w') as newfile:
        for line in oldfile:
            if not any(to_archive in line for to_archive in to_archive):
                newfile.write(line)
                f.close()
    import os
    os.remove("todo.txt")
    os.rename("todoreplace.txt", "todo.txt")
    remove_numbering()
    give_newnumber()

exit()
