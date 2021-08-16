from numpy import random
list_number = random.randint(1, 20, 10)
tuple_number = tuple(list_number)
print(tuple_number)
print(f"Sum: {sum(tuple_number)} Max: {max(tuple_number)}")