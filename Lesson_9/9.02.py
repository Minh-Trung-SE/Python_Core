from numpy import random
new_dict = {i: random.randint(1, 10) for i in range(8, -1, -1)}
print(new_dict)
print(sorted(new_dict)[-1:-4:-1])
print(new_dict)
for key in sorted(new_dict)[-1:-4:-1]:
    print(new_dict.get(key), end=" ")