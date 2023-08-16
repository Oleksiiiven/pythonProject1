def prime_verification(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


number = int(input("Enter a number: "))

if prime_verification(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")