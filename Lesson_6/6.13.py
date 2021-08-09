# 6.13 exercise // find x in source
txt = "Hello, welcome to my world."


def fill_all_index(msg, letter):
    index = []
    for i in range(1, len(msg)):
        if msg[i] == letter:
            index.append(i)
    return index


print(fill_all_index(txt, "o"))
# [5, 12, 17, 23]