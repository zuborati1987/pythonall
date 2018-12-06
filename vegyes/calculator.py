#simple calculator homework
#2018.10.22

def calculation():
    if operation == "+":
        print ("Result is: ")
        print (x+y)
    elif operation == "-":
        print ("Result is: ")
        print (x-y)
    elif operation == "*":
        print ("Result is: ")
        print (x*y)
    elif operation == "/":
        print ("Result is: ")
        print (x/y)
    else:
        print ("Exiting...")
        exit()

try:
    x = int(input("Please enter a number, or a letter to exit: "))
    y = int(input("Please enter another number, or a letter to exit: "))
    operation = input("Please enter an operation, or a letter to exit: ")
    calculation()
except(ValueError):
    print ("Exiting...")
    exit()








