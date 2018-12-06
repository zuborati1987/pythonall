# calculates the retirement year
# 2018.10.19


import datetime



def get_user_age():
    x = input('Give me your age: ')
    x = int (x)
    return x

def get_user_retireyear():
    x = input('Your ideal retirement year: ')
    x = int(x)
    return x


def show_formatted_msg(age, ideal_retired_year_start, cur_year):
    print('your age is {}, your ideal retirement year start is {}, {} '.format(age, ideal_retired_year_start, cur_year))


def main():
    current_year = datetime.datetime.now().year
    age = get_user_age()
    ideal_retired_year_start = get_user_retireyear()
    ret_year = current_year + (ideal_retired_year_start - age)
    show_formatted_msg(age, ideal_retired_year_start, current_year, ret_year)

if __name__=='__name__':
    main()