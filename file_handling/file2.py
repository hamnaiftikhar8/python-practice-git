import os

import os

def file_create(filename):
    try:
        # Ensure directory exists before creating the file
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("Hello this is me Hamna. An ASE at Devsinc.")
        print(f"File '{filename}' has been created successfully.")
    except IOError as e:
        print(f"Error creating file '{filename}': {e}")


def write_file(filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("FILE TO BE UPDATED.")
    except IOError as e:
        print("Error writing file")

def append(filename, text):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a') as f:
            f.write(text)
    except IOError as e:   
        print("Error in appending.")

def rename(filename, newfile):
    try:
        # Ensure directory exists before renaming the file
        os.makedirs(os.path.dirname(newfile), exist_ok=True)
        
        os.rename(filename, newfile)
        print(f"File '{filename}' has been renamed to '{newfile}' successfully.")
    except IOError as e:
        print(f"Error renaming file '{filename}' to '{newfile}': {e}")

def delete(filename):
    try:
        os.makedirs(os.path.dirname(newfile), exist_ok=True)
        os.remove(filename)
    except IOError as e:        
        print("THe file has been deleted.")



if __name__ == "__main__":
    file_path = "/home/dev/Desktop/Devsinc/python-practice/basics/file_handling/file_text.txt"
    newfile = "/home/dev/Desktop/Devsinc/python-practice/basics/file_handling/newfile.txt"
    file_create(file_path)
    rename(file_path, newfile)
    write_file(file_path)
    append(file_path, "A new text has been appended.")
    delete(file_path)



