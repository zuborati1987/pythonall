# create a simple math script
# 2018.10.19


def get_Int_Input():
    x = input('Get int number: ')
    x = int(x)
    return x


def get_sum_str(a, b):
    sum = "{} + {} = {}".format(a, b, a + b)
    return sum


def get_substract_str(a, b):
    sub = "{} - {} = {}".format(a, b, a - b)
    return sub


def show_operates(a, b):
    print('{} {} {} {}'.format(a, b, get_subtract_str(a, b), get_sum_str(a, b)))


def main():
    a = get_Int_Input()
    b = get_Int_Input()
    show_operates(a, b)


if __name__ == '__main__':
    main()
