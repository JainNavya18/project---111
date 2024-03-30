import os
import shutil

from_dir = "C:/Users/jainn/OneDrive/Pictures"
to_dir = "C:/Users/jainn/OneDrive/Documents"

list_of_files = os.listdir(from_dir)
print("List of files in the source directory:", list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print("File:", name, "Extension:", extension)

