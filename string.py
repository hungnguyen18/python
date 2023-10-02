def split_words():
    string = input("Enter a string: ")
    words = string.split(" ")
    for word in words:
        print(word)

split_words()

def concatenate_strings():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    # Concatenate the two strings
    string = string1 + string2

    # Print the lowercase string
    print(string)

    # Print the uppercase string
    print(string.upper())

concatenate_strings()

def calculate_string_length():
    string = input("Enter a string: ")
    string_length = len(string)
    half_length = string_length // 2

    # Print the length of the string
    print("String length:", string_length)

    # Print the characters from the beginning to half the length of the string
    print("Characters from the beginning to half the length of the string:", string[:half_length])

    # Print the characters from half the length of the string to the end
    print("Characters from half the length of the string to the end:", string[half_length:])

calculate_string_length()
