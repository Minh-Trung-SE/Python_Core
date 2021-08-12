import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_a = []
if len(a) >= 5:
    for i in range(5):
        new_a.append(a[np.random.randint(0, len(a))])
print(new_a)
