import os
import sys
import pathlib
import zipfile

input_directory = input("Enter the directory name that you want to backup: ")

if not os.path.isdir(input_directory):
    print("Directory", input_directory, "doesn't exist")
    sys.exit(0)

source_directory = pathlib.Path(input_directory)

with zipfile.ZipFile("myZip.zip", "w") as zip_archive:
    for file_path in source_directory.rglob("*"):
        zip_archive.write(file_path, file_path.relative_to(source_directory))

if os.path.isfile("myZip.zip"):
    print("Archive", "myZip.zip", "created successfully")
else:
    print("Error in creating the ZIP archive")
