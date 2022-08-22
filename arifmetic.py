

def arithmetic(a, b, c):
    if c == "+":
        return (a + b)
    elif c == "-":
        return (a - b)
    elif c == "*":
        return (a * b)
    elif c == "/":
        if b == 0:
            return "Деление на ноль"
        return (a / b)
    else:
        return ("Неизвестная операция")


if __name__ == '__main__':

    a = int(input("First number = "))
    b = int(input("Second number = "))
    c = input("what to do with numbers ")
    print("Результат ", arithmetic(a ,b ,c))