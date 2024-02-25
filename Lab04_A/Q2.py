def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            print(line.strip())

path = "./Lab04/a/"
filename = "q2.txt"
filename_lst = "q2_lst.txt"

write_to_file(path + filename, "This is new content")
print("Done writing")
read_file_contents(path + filename)

append_to_file(path + filename, "This is appended content")
print("Opening file again..")
read_file_contents(path + filename)

lst = ['Name: Emma', 'Address: 221 Baker Street', 'City: London']
write_list_to_file(path + filename_lst, lst)
print("Done writing list")
read_file_contents(path + filename_lst)
