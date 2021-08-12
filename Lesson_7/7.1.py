from numpy import random


def calc_array(arr):
    product_array = 1
    if len(arr) == 0:
        return 0, 0
    else:
        for i in arr:
            product_array *= i
    sum_array = sum(arr)
    return sum_array, product_array


a = random.randint(0, 10, size=int(input("Enter size of array: ")))
print(f"Array is: {a}")
total, product = calc_array(a)
print(f"{total}, {product}")
