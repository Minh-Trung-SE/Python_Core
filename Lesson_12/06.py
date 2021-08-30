try:
    line = input("Enter string to write of end file: ")
    with open('06.txt', mode='a', encoding='utf8') as file_06:
        file_06.write(line)
    print("Write file success!")
except FileNotFoundError:
    print("File not found!")
