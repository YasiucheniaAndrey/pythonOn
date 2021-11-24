  # todo remove blank line
def square(x):
    result = ((x*4), (x**2), (x*(2**(1/2))))
    print (type(result))  # todo don't print inside function

    print("Периметр = ", result[0],'\n'
          "Площадь = ", result[1],'\n'
          "Диагональ = ", result[2])

## todo too many blank lines


square(int(input("Сторона квадрата равна ")))

