def is_prime(a):
    i = 2

    while i < a:
        if a % i == 0:
            return False
        i += 1

    return True



print(is_prime(int(input("Enter number to check "))))
