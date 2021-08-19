data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
new_dict = {}
for i in range(len(data)):
    list_key_item = list(data[i].keys())
    key_item = data[i].get(list_key_item[0])
    value_item = data[i].get(list_key_item[1])
    print(key_item, value_item)
    if key_item not in new_dict:
        new_dict[key_item] = value_item
    else:
        new_dict[key_item] += value_item

print(new_dict)