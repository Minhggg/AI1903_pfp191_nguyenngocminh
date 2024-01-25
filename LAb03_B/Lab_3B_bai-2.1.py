#2.1


import string

def clean_string(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s

def is_anagram(str1, str2):
    str1_cleaned = clean_string(str1)
    str2_cleaned = clean_string(str2)
    
    # Count the occurrences of each character in both strings
    count_str1 = {}
    count_str2 = {}
    
    for char in str1_cleaned:
        count_str1[char] = count_str1.get(char, 0) + 1
        
    for char in str2_cleaned:
        count_str2[char] = count_str2.get(char, 0) + 1
    
    # Check if the character counts are equal
    return count_str1 == count_str2

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    if is_anagram(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == "__main__":
    main()
