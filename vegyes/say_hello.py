#say hello program
#2018.10.09.

import platform

def show_version():
    print(platform.python_version())


def get_Name_Input():
    name = input('What is your name? ')
    return name

def show_greeting(user_name):
    print("{}, nice to meet you! ".format(user_name))


def main ():
    un = get_Name_Input ()
    show_greeting(un)


if __name__=='__main__':
    main()