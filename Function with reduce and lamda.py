from functools import reduce


def multiply_numbers(numbers):
    results = reduce(lambda x, y: x * y, numbers)
    return results


numbers = [1, 2, 3, 4, 5, 6, 7]
result = multiply_numbers(numbers)
print("Result:", result)
