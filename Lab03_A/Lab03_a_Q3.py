#3.1A
def create_mixed_string(original_string):
    # Calculate the length of the original string
    length = len(original_string)
    
    # Calculate the starting index for the middle four characters
    middle_index = (length - 4) // 2
    
    # Extract the middle four characters
    mixed_string = original_string[middle_index:middle_index + 4]
    
    return mixed_string

# Test cases
test_cases = ["billdecstran", "hosonghu"]

for original_string in test_cases:
    print("Original string is", original_string)
    print("Middle four chars are:", create_mixed_string(original_string))


#3.2A

def append_middle(s1, s2):
    # Calculate the length of the first string
    length_s1 = len(s1)
    
    # Calculate the middle index of the first string
    middle_index = length_s1 // 2
    
    # Insert the second string in the middle of the first string
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    
    return s3

# Test the function
s1 = input("Enter the first string (s1): ")
s2 = input("Enter the second string (s2): ")
s3 = append_middle(s1, s2)
print("New string (s3):", s3)


#3.3A

def extract_chars(s):
    length = len(s)
    if length % 2 == 0:
        middle_char = s[length // 2 - 1]
    else:
        middle_char = s[length // 2]
    return s[0] + middle_char + s[-1]

def combine_strings(s1, s2):
    combined_string = ""
    combined_string += extract_chars(s1)
    combined_string += extract_chars(s2)
    return combined_string
#test
s1 = "america"
s2 = "japan"
output = combine_strings(s1, s2)
print(output)


#3.4A

def arrange_characters(input_str):
    lowercase = ''
    uppercase = ''
    for char in input_str:
        if char.islower():
            lowercase += char
        else:
            uppercase += char
    return lowercase + uppercase

#tét
input_str = "PyNaTive"
output_str = arrange_characters(input_str)
print(output_str)  # Output: "yaivePNT"


#3.5A


def count_characters(string):
    letters = 0
    digits = 0
    specials = 0

    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            specials += 1

    return letters, digits, specials

#tét

input_string = "P@yn2at&dfsdfd&^^^&^^&^#iev5"
letter_count, digit_count, special_count = count_characters(input_string)
print("Letters:", letter_count)
print("Digits:", digit_count)
print("Special Symbols:", special_count)
