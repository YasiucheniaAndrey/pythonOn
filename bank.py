# todo python file name should start from the lowercase letter
def bank(ammount, years):  # todo what is a? variable names should be self-describing
    i = years
    percentPerYear = 6# add whitespaces like `i = years`
    while i > 0:  #  you can use a for loop here: `for i in range(years):` - it is more readable
        ammount = (1+percentPerYear/100) * ammount  # todo 1.1 should be a variable
        i -= 1
    return ammount

if __name__ == "__main__":
    ammount = int(input("Сколько денег "))
    years = int(input("На сколько лет? "))

    print("Через ", years, " лет будет ", bank(ammount, years), " денег")

