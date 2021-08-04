str_root = input("Enter string to mix two first letter and last two letter: ")
if len(str_root) < 4:
    print("Can't mix word from this string thank!")
else:
    str_root = str_root[:2] + str_root[-2:len(str_root)]
    print(str_root)