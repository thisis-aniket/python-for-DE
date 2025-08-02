"""
4. Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that. 
"""

import os

# Specify the directory path
directory_path = '/'  # Replace with your directory path

try:
    # List all entries in the directory
    entries = os.listdir(directory_path)
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
