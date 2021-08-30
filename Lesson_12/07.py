try:
    with open('05.txt', mode='r', encoding='utf8') as file_1:
        data_file_1 = file_1.read()
    with open('06.txt', mode='r', encoding='utf8') as file_2:
        data_file_2 = file_2.read()
    data_file_1 += "\n"
    data_file_1 += data_file_2
    with open('07.txt', mode='a', encoding='utf8') as file_concat:
        file_concat.write(data_file_1)
    print("Concat file success!")
except FileNotFoundError:
    print("File not found!")
