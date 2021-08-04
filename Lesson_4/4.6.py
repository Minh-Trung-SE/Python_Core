import re
# defining string
str1 = input("Enter string: ")

# defining substring
substr = input("Enter substring: ")

print("The original string is: " + str1)

print("The substring to find: " + substr)

result = [index.start() for index in re.finditer(substr, str1)]

print("The start indices of the substrings are : " + str(result))