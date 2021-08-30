import os


def get_file_size(file):
    file.seek(0, os.SEEK_END)
    return file.tell()


try:
    file_input = open('07.txt')
    print("Size file: ", get_file_size(file_input))
except FileNotFoundError:
    print("File not found!")
