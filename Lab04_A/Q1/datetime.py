import os
from datetime import datetime

def create_file_with_datetime():
    # Get current date and time
    current_datetime = datetime.now()
    
    # Format the datetime to include in the file name
    datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the file name with the formatted datetime
    file_name = "file_{}.txt".format(datetime_str)
    
    # Create the file
    with open(file_name, 'w') as file:
        file.write("This file was created with the current date and time.")

    print("File '{}' created successfully.".format(file_name))

if __name__ == "__main__":
    create_file_with_datetime()
