def bank(a, years):
    i=years
    while i > 0:
        a = 1.1*a
        i -= 1

    print("Через ", years,  " лет будет ", a , " денег")


bank(int(input("Сколько денег ")), int(input("На сколько лет? ")))

