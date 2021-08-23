# str_1 = """Line 1
# Line 2"""
# print(str_1)
# print(type(str_1))
# print(isinstance(str_1, str))
# file = open("file.txt", "r")
# str_1 = file.read()
#
# for cha in str_1:
#     print(cha.isdigit(), cha)
#
# a = 5
# print(str(a).isdigit())
#
# s2 = str_1.split(" ")
# for sub in s2:
#     print(sub)
#
# import numpy as np
# a = [[3, -4, 5], [2, -3, 1], [3, -3, 1]]
# a = np.array(a)
# print(np.lineal.inv(a))
# my_tuple = ('one',)
# print(type(my_tuple))
# print(f"{my_tuple}")
class Car:
    color = 'Blue'

    def __init__(self, color="Black"):
        self.color = color

    def show_color(self):
        print(self.color)


car = Car("red")
car.show_color()
