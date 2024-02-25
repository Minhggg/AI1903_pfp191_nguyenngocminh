import os

def create_file_with_permission(file_name, permission):
    try:
        # Create file
        with open(file_name, 'w') as file:
            file.write("This is a test file.")

        # Set the permissions
        os.chmod(file_name, permission)

        print(f"File '{file_name}' created successfully with permission {permission:o}.")
    except OSError as e:
        print(f"Error occurred while creating the file: {e}")

if __name__ == "__main__":
    file_name = "example.txt"
    permission = 0o644  
    create_file_with_permission(file_name, permission)
