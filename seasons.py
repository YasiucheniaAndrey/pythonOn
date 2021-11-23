def season (month):

    if 0<month<2 or month==12:
        print('Now is winter')
    elif 3<=month<6:
        print('Now is spring')
    elif 6<=month<9:
        print("Now is autumn")
    elif 9<=month<12:
        print("Now is winter")
    else:
        print("input is not month")








season(int(input("Month please ")))