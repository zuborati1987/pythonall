num_lines = 1
with open("todo.txt", 'r') as f:
    for line in f:
        num_lines += 1
f.close()


def remove_numbering():
    f = open("todo.txt")
    lines = f.readlines()
    f.close()
    f = open("todo.txt", 'w')
    for line in lines:
        f.write(line[1:])
    f.close()


remove_numbering()


def give_newnumber():
    with open('todo.txt', 'r') as program:
        data = program.readlines()

    with open('todo.txt', 'w') as program:
        for (number, line) in enumerate(data):
            program.write('%d  %s' % (number + 1, line))
    f.close()


give_newnumber()

f.close()
