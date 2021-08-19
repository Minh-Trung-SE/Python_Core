from numpy import random
my_dict = {i: random.randint(1, 10) for i in range(5)}
print(my_dict)
max_key = max(my_dict.keys(), key=(lambda index: my_dict[index]))
min_key = min(my_dict.keys(), key=(lambda index: my_dict[index]))
print(f"Max value: {my_dict.get(max_key)}")
print(f"Min value: {my_dict.get(min_key)}")