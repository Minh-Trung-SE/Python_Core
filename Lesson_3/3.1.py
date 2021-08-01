import math


def calc_delta(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    return delta


# Get int number and handle exception
def get_int(prompt):
    int_number = 0
    while True:
        try:
            int_number = int(input(prompt))
            break
        except ValueError:
            print("Not valid int number!")
    return int_number


def calc_function():
    a, b, c = get_int("Enter a: "), get_int("Enter b: "), get_int("Enter c: ")
    if a == 0 and c == 0:
        print("Function have many solution!")
        return
    if a == 0:
        x = (-1 * c) / b
        print(f"This function only one solution x = {x}")
        return
    delta = calc_delta(a, b, c)
    if delta == 0:
        x = (-1 * b) / (2 * a)
        print(f"X1 = X2 = {x}")
    elif delta < 0:
        print("Function not have solution")
    else:
        print(f"X1 = {(-1 * b + math.sqrt(delta)) / (2 * a)}")
        print(f"X2 = {(-1 * b - math.sqrt(delta)) / (2 * a)}")
        return


def main():
    calc_function()
    return


if __name__ == "__main__":
    main()
