input_str = 'Stringings'
count = {}
for i in input_str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
print(count)