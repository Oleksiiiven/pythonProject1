def get_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print("Even numbers:", even_numbers)
