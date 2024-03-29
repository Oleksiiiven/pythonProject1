def palindrome_verification(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]


input_string = input("Enter a string: ")

if palindrome_verification(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
