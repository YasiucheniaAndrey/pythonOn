# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция
# , которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
# то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку
# "Неизвестная операция".

def arithmetic(a,b,c):  # add whitespaces
    if c == "+":
        print(a+b)  # don't use prints here. Use `return` instead
    elif c == "-":
        print (a-b)  # add whitespaces
    elif c == "*":
        print (a*b)
    elif c == "/":
        print (a/b)
    else:
        print("Неизвестная операция")  # don't use prints here. Use `return` instead.

a = int(input("First number = "))
b = int(input("Second number = "))
c = input("what to do with numbers ")

arithmetic(a,b,c) # add whitespaces
