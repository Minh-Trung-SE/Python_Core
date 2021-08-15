def min_2nd(data_source):
    print(min(data_source, key = lambda element: element[1]))

list_of_tuples = [(9, 2, 7), (6, 8, 4), (3, 5, 1)]
min_2nd(list_of_tuples)