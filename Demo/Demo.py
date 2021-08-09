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
def func_greet(name, msg):
    print(f"Hello {name}, {msg}")


# func_greet("Trung")
# func_greet("Trung", "Minh", "An")
func_greet()
