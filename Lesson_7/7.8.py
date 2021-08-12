from numpy import random
a = random.randint(0, 20, size=8)
print(a)
count = 0
for i in range(len(a) - 1):
    for j in range((i + 1), len(a)):
        if a[i] > a[j]:
            count += 1
            # print(f"i: {i} j: {j}", end=" || ")
print(count)