def count_total_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            total_words = sum(len(line.split()) for line in file)
        print("Total number of words in the file:", total_words)
    except IOError:
        print(f"Error: could not count words in file {filename}")


def display_short_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            short_words = ' '.join(word for line in file for word in line.split() if len(word) < 4)
            print(short_words)
    except IOError:
        print(f"Error: could not display words in {filename}")

if __name__ == '__main__':
    filename1 = "story.txt"
    count_total_words(filename1)

    filename2 = "story.txt"
    display_short_words(filename2)

