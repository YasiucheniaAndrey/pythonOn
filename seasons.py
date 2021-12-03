def season(month):  # remove whitespace `def season(month):`

    if 0 < month < 2 or month == 12:  # add whitespaces `if 0 < month < 2 or month == 12:`
        return ('Now is winter')  # use return instead print
    elif 3 <= month < 6:
        return ('Now is spring')
    elif 6 <= month < 9:
        return ("Now is autumn")
    elif 9 <= month < 12:
        return ("Now is winter")
    else:
        return ("input is not month")

# todo add a condition https://github.com/YasiucheniaAndrey/pythonOn/blob/main/main.py#L13
if __name__ == "__main__":

season(int(input("Month please ")))
