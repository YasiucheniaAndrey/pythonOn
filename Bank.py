# todo python file name should start from the lowercase letter
def bank(a, years):  # todo what is a? variable names should be self-describing
    i=years  # add whitespaces like `i = years`
    while i > 0:  #  you can use a for loop here: `for i in range(years):` - it is more readable
        a = 1.1*a  # todo 1.1 should be a variable
        i -= 1

    print("Через ", years,  " лет будет ", a , " денег")  # todo do not use prints inside the function. It should return some result

# todo the code shouldn't run if the module is imported somewhere
# please add a clause: `if __name__ == "__main__":`
bank(int(input("Сколько денег ")), int(input("На сколько лет? ")))

