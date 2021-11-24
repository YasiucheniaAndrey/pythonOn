def season (month):  # remove whitespace `def season(month):`

    if 0<month<2 or month==12:  # add whitespaces `if 0 < month < 2 or month == 12:`
        print('Now is winter')  # use return instead print
    elif 3<=month<6:
        print('Now is spring')
    elif 6<=month<9:
        print("Now is autumn")
    elif 9<=month<12:
        print("Now is winter")
    else:
        print("input is not month")



# todo too many blank lines



# todo add a condition https://github.com/YasiucheniaAndrey/pythonOn/blob/main/main.py#L13
season(int(input("Month please ")))
