
def square(x):
    result = ((x*4), (x**2), (x*(2**(1/2))))
    print (type(result))

    print("Периметр = ", result[0],'\n'
          "Площадь = ", result[1],'\n'
          "Диагональ = ", result[2])




square(int(input("Сторона квадрата равна ")))

