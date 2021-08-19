from numpy import random

new_dict = {i: random.randint(1, 10, 5).tolist() for i in range(5)}
print(new_dict)
for key in new_dict:
    print(new_dict.get(key)[-1])