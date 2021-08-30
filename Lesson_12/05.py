line = ''
try:
    file_05 = open('05.txt', mode='r', encoding='utf8')
    lines = int(input("Enter number line to read: "))
    while lines > 0:
        line = file_05.readline()
        if line == '':
            file_05.close()
            break
        else:
            print(line, end="")
        lines -= 1
except FileNotFoundError:
    print("File not found!")
except TypeError:
    print("Input number lines invalid!")
