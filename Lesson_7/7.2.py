from numpy import random, max, min

array_random = random.uniform(0, 100, size=int(input("Enter size of array: ")))
print(array_random)
print(f"Max of array: {max(array_random)}")
print(f"Min of array: {min(array_random)}")