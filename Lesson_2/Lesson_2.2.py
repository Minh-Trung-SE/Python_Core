import math

x = float(input("Enter value of X: "))
y = float(input("Enter value of Y: "))
z = float(input("Enter value of Z: "))

f = (x + y + z) / (math.pow(x, 2) + math.pow(y, 2) + 1) - abs(x - z * math.cos(y))
print(round(f, 2))
