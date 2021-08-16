# Counting elements in list until it's tuple.
def count(data_source):
    result = 0
    for element in data_source:
        if isinstance(element, tuple):
            return result
        else:
            result += 1

data = [1,2,5,6,(9,9)]
print(f"{count(data)}")