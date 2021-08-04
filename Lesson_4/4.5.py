str_input = input("Enter string to show only digit: ")
for i in range(len(str_input)):
    if str_input[i].isdigit():
        print(str_input[i], end=" ")