from numpy import random

dict_1 = {i: random.randint(1, 10) for i in range(random.randint(1, 10))}
dict_2 = {i: random.randint(1, 10) for i in range(random.randint(4, 10))}
print(dict_1)
print(dict_2)
for key in set(dict_1.keys()).intersection(dict_2.keys()):
    print(dict_1.get(key), end=" ")
