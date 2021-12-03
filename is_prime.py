def is_prime(a):
    i = 2 # no sense to divide on 1 so start from 2

    while i < a:
        if a % i == 0:
            return False
        i += 1

    return True


if __name__ == "__main__":
    number = int(input("Enter number to check "))
    result = is_prime(number)
    print("Is number is prime?? ----->>>> ", result)
