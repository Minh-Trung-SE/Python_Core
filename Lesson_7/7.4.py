from numpy import random
root_array = random.randint(0, 100, size=int(input("Enter size array to create random element: ")))
split_index = int(input("Enter index to split: "))
if split_index < 0 or split_index > len(root_array):
    print("Out of range of array!")
else:
    first_part = root_array[:split_index]
    last_part = root_array[split_index:]

print(first_part)
print(last_part)