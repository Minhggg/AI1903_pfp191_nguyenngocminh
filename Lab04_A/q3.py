import os

path = "./Lab04/a/"
filename = f"{path}test.txt"

def read_from_start(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, os.SEEK_SET)
        print(file.read())

def append_to_end(file_path, content):
    with open(file_path, 'a') as file:
        file.seek(0, os.SEEK_END)
        file.write(f"\n{content}")
        print(f"File handle at: {file.tell()}")

def read_from_current_position(file_path, offset):
    with open(file_path, 'r') as file:
        current_position = file.tell()
        new_position = current_position + offset
        file.seek(new_position, os.SEEK_SET)
        print(file.read())

read_from_start(filename)
print("*************")
append_to_end(filename, "This content is added to the end of the file")
print("*************")
read_from_current_position(filename, 3)
print("*************")
