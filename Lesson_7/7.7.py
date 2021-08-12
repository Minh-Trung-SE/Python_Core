from numpy import random
a = random.randint(0, 20, size=10)
b = random.randint(0, 20, size=10)
print(a)
print(b)
c = set(a) & set(b)
print(c)
