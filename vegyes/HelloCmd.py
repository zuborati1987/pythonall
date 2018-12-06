#Hello with name as cmd line argument
#2018.10.22

import sys

if len(sys.argv) <= 1:
    print("Hello world!")
else:
    name = sys.argv[1]
    print("Hello " + name + "!")