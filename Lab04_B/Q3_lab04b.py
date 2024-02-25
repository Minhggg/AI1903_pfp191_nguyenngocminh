def count_uppercase(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            uppercase_count = sum(1 for char in file.read() if char.isupper())
        print("Uppercase characters count:", uppercase_count)
    except IOError:
        print("Error: Unable to count uppercase characters in", filename)

def count_target_words(filename):
    try:
        target_words = {'this', 'these'}
        with open(filename, 'r', encoding='utf-8') as file:
            words_count = sum(line.lower().count(word) for line in file for word in target_words)
        print("Occurrences of 'this' and 'these':", words_count)
    except IOError:
        print("Error: Unable to count occurrences of 'this' and 'these' in", filename)

if __name__ == '__main__':
    filename1 = "story.txt"
    count_uppercase(filename1)

    filename2 = "article.txt"
    count_target_words(filename2)

