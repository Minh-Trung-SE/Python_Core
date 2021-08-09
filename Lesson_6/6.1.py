def max_min(*numbers):
    return max(numbers), min(numbers)


max_number, min_number = max_min(9, 8, 6, 15)
print(f"Max: {max_number}")
print(f"Min: {min_number}")
