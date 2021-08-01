import math


def get_float(prompt):
    float_number = 0
    while True:
        try:
            float_number = float(input(prompt))
            break
        except ValueError:
            print("Not valid number!")
    return float_number


def check_is_type_triangle(edge_a, edge_b, edge_c):
    if pow(edge_a, 2) == pow(edge_b, 2) + pow(edge_c, 2) or\
            pow(edge_b, 2) == pow(edge_a, 2) + pow(edge_c, 2) or\
            pow(edge_c, 2) == pow(edge_a, 2) + pow(edge_b, 2):
        print("This is right triangle!")
    elif edge_a == edge_b and edge_b == edge_c:
        print("This is equilateral triangle!")
    elif edge_a == edge_b or edge_a == edge_c or edge_b == edge_c:
        print("This is isosceles triangle!")
    else:
        print("This is triangle!")


def check_is_triangle(value_a, value_b, value_c):
    if value_a + value_b > value_c and value_a + value_c > value_b and value_b + value_c > value_a:
        check_is_type_triangle(value_a, value_b, value_c)
    else:
        print("Sorry value edge is not triangle!")


a = get_float("Enter value edge A: ")
b = get_float("Enter value edge B: ")
c = get_float("Enter value edge C: ")
check_is_triangle(a, b, c)
