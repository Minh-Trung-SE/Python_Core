from numpy import random

tuple_a = tuple(random.randint(1, 40, 10))
tuple_b = tuple(random.randint(1, 20, 10))
print(tuple_b)
print(tuple_a)

tuple_intersection = tuple(set(tuple_a).intersection(set(tuple_b)))
print(tuple_intersection)
