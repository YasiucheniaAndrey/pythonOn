def is_year_leap(year):
    z = year % 4

    if z == 0:
        print("True")
    else:
        print("False")

a = int(input('введите год пжлста '))

is_year_leap(a)
