from numpy import random

a = random.randint(1, 20, size=20).tolist()
print(a)
max_exist = 0
index_max_exist = 0
for i in range(len(a)):
    exist = a.count(a[i])
    if max_exist < exist:
        max_exist, index_max_exist = exist, i

print(f"Element {a[index_max_exist]} exist {max_exist} time!")
