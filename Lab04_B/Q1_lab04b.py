def display_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def count_non_t_lines(filename):
    try:
        count = 0
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith('T'):
                    count += 1
        print(f"No of lines not starting with 'T' = {count}")
        
    except IOError:
        print("Error: could not count the number of lines " + filename)
            
if __name__ == '__main__':
    filename1 = "poem.txt"
    display_file_content(filename1)

    filename2 = "story.txt"
    count_non_t_lines(filename2)
