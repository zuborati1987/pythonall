# saves ideas as a lisst
# 2018.10.22

import sys

f = open("ideas.txt", "a+")
x = input("What ideas do you have today? ")
if x == ("None"):
    f = open("ideas.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()
else:
    f.write(x + " ")
    f = open("ideas.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        f.close()
f.close()
