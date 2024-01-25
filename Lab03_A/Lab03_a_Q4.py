#4.1A


def remove_non_integers(input_string):
    return ''.join(char for char in input_string if char.isdigit())
 
str1 = "i am 25 years and 10 months"
result = remove_non_integers(str1)
print( result)


#4.2A

import string

def remove_special_symbols(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

# Test 
given_string = input("enter given_string: ")
result = remove_special_symbols(given_string)
print(result)


#4.3A


def remove_empty_strings(strings_list):
    return list(filter(lambda x: x.strip(), strings_list))

# Test 
given_list = ["Emma", "john", "", "Kenny", "none", "eric", ""]
result = remove_empty_strings(given_list)
print("Original list of string:", given_list)
print("after removing empty strings:", result)


#4.4A

str1 = "emma-is-data-scientist"
substrings = str1.split("-")

# Display each substring
for substring in substrings:
    print(substring)
