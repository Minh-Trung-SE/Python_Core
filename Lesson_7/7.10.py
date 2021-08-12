from numpy import random

a = random.randint(0, 10, size=20)
b = []
print(a)
for i in a:
    if i not in b:
        b.append(i)
print(b)
# another way using set
print(set(a))
