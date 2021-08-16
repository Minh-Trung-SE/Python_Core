from numpy import random

set_a = set(random.randint(1, 20, 10))
set_b = set(random.randint(1, 20, 10))
print(set_a)
print(set_b)
print(f"Set A disjoint Set B: {set_a.isdisjoint(set_b)}")
print(f"Set A is subset Set B: {set_a.issubset(set_b)}")
print(f"Set A is Supper of Set B: {set_a.issuperset(set_b)}")
# Difference_update
set_c = set_a.copy()
set_a.difference_update(set_b)
print(set_a)

# Intersection Update
set_a = set_c.copy()
set_a.intersection_update(set_b)
print(set_a)

# Symmetric difference update
set_a = set_c.copy()
set_a.symmetric_difference_update(set_b)
print(set_a)

