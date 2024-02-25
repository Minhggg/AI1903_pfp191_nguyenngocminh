def display_with_hashes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            formatted_content = '#'.join(content)
            print(formatted_content)
    except IOError:
        print("Error: could not display with hashes " + filename)

def replace_J_with_I(filename):
    try:
        corrected_text = ""
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                corrected_line = line.replace('J', 'I')
                corrected_text += corrected_line
        print(corrected_text)
    except IOError:
        print("Error: could not replace J with I " + filename)

if __name__ == '__main__':
    filename1 = "matter.txt"
    display_with_hashes(filename1)
    
    filename2 = "WORDS.TXT"
    replace_J_with_I(filename2)

