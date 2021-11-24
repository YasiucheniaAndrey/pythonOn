# todo please use snake_case for file names in python (ex. `leap_year.py`)
def is_year_leap(year):
    z = year % 4

    if z == 0:
        print("True")  # todo don't print inside function. It should return something and then you may use it to output for the user
    else:
        print("False")

a = int(input('введите год пжлста '))

# todo add condition like here https://github.com/YasiucheniaAndrey/pythonOn/blob/main/main.py#L13
is_year_leap(a)
