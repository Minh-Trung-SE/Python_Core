def common_member(data1,data2):
    data1_set = set(data1)
    data2_set = set(data2)
    if len(data1_set.intersection(data2_set)) > 0:
        return True
    return False


tuplex1 = (1, 2, 3, 4)
tuplex2 = (5, 6, 7, 8, 9)
print(common_member(tuplex1, tuplex2))

