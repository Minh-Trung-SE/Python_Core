a = ['sbcs', 'abdhgdbfcmja', 'qaseddcvd', 'adghda']
count = 0
for i in a:
    if len(i) >= 2:
        if i[0] == i[-1]:
            count += 1
print(count)