def find_max_word(str_input):
    str_input = str_input.split(" ")
    max_len_index = 0
    for i in range(len(str_input)):
        if len(str_input[max_len_index]) < len(str_input[i]):
            max_len_index = i
    return str_input[max_len_index]


str_a = input("Enter your string: ")
print(find_max_word(str_a))
print(str_a)
