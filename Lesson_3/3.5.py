import math

while True:
    epsilon_value = float(input("Enter value epsilon: "))
    if 1 > epsilon_value > 0:
        break
    else:
        print("Invalid epsilon!")

epsilon = 1
i = 0
while True:
    i += 1
    epsilon += (1 / math.factorial(i))
    if 1 / math.factorial(i) < epsilon_value:
        break

print(f"{epsilon:.3}")
