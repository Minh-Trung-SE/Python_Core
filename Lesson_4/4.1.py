str_root = input("Enter string to replace all letter same first letter: ")
str_replace = str_root.replace(str_root[0], "$")
str_root = str_root[0] + str_replace[1:]
print(str_root)
