from numpy import random
new_dict = {i: random.randint(1, 10) for i in range(5)}
print(new_dict)
product = 1
for i in range(len(new_dict)):
    product *= new_dict.get(i)
print(product)