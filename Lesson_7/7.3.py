from numpy import random

root_array = random.randint(0, 100, size=int(input("Enter size array to create random element: ")))
concat_string = input("Enter your string: ")
new_array = []
for i in root_array:
    new_array.append(str(i) + concat_string)

print(new_array)
