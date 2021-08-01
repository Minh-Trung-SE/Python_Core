import math


def get_int(prompt):
    int_number = 0
    while True:
        try:
            int_number = int(input(prompt))
            break
        except ValueError:
            print("Not valid int number!")
    return int_number


def get_float(prompt):
    float_number = 0
    while True:
        try:
            float_number = float(input(prompt))
            break
        except ValueError:
            print("Not valid number!")
    return float_number


print("S1")
n = get_int("Enter N: ")
x = get_float("Enter X: ")
sum_sequence = 1
for i in range(1, (n + 1)):
    sum_sequence += math.pow(x, i)
print(round(sum_sequence, 2))

print("S2")
n = get_int("Enter N: ")
x = get_float("Enter X: ")
sum_sequence = 1
for i in range(1, (n + 1)):
    sum_sequence += math.pow(-1, i) * math.pow(x, i)
print(round(sum_sequence, 2))

print("S3")
n = get_int("Enter N: ")
x = get_float("Enter X: ")
sum_sequence = 1
for i in range(1, (n + 1)):
    sum_sequence += pow(x, i) / math.factorial(i)
print(round(sum_sequence, 2))
