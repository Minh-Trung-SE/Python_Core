from numpy import random
new_dict = {i: random.randint(1, 10) for i in range(5)}
print(new_dict)
new_dict = dict(sorted(new_dict.items(), key=lambda element: element[1], reverse=True))
# sorted(new_dict.items(), key=lambda element: element[1], reverse=True)
# new_dict.items() ==> [[key, value], [key, value]...]
# key=lambda element: element[1] get value
for key in list(new_dict.keys())[:3]:
    print(new_dict.get(key), end=" ")