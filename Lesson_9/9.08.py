text = input("Enter your string: ")
list_word = text.split(" ")
my_dict = {}
for key in list_word:
    if key not in my_dict:
        my_dict[key] = 1
    else:
        my_dict[key] += 1

print(my_dict)