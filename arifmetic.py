# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция
# , которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
# то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку
# "Неизвестная операция".

def arithmetic(a,b,c):  # todo add whitespaces
    if c == "+":
        print(a+b)  # todo don't use prints here. Use `return` instead
    elif c == "-":
        print (a-b)  # todo add whitespaces
    elif c == "*":
        print (a*b)
    elif c == "/":
        print (a/b)
    else:
        print("Неизвестная операция")  # todo don't use prints here. Use `return` instead.

a = int(input("First number = "))
b = int(input("Second number = "))
c = input("what to do with numbers ")

# todo add condition https://github.com/YasiucheniaAndrey/pythonOn/blob/main/main.py#L13
arithmetic(a,b,c) # add whitespaces
