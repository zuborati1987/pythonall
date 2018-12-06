# count the number of characters
# 2018.10.19.

def get_Name_Input():
    name = input('Give me an input! ')
    return name

def show_input_and_lenght(input_line):
    print('{} is {} long.'.format(input_line, len(input_line)))







def main():
    line = get_Name_Input()
    show_input_and_lenght(line)
    
if __name__=='__main__':
    main()