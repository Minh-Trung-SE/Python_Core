from numpy import random

tuple_a = (1, 1, 1, 1, 1, 1, 1)
tuple_b = random.randint(1, 20, 10)


def check_same(tuple_arg):
    return tuple(tuple_arg).count(tuple_arg[0]) == len(tuple_arg)


print(f"Tuple: {tuple(tuple_a)} all element is same is: {check_same(tuple_a)}")
print(f"Tuple: {tuple(tuple_b)} all element is same is: {check_same(tuple_b)}")
