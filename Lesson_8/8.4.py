def last(n):
    return n[-1]

def sort_list_last(data_source):
  return sorted(data_source, key=last)

print(sort_list_last([(1, 5), (1, 2), (1, 4), (1, 3), (1, 1)]))
