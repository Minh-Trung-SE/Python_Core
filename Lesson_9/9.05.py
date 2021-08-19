sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
new_dict = {key: sampleDict.get(key) for key in keys}
print(new_dict)
print(type(new_dict.items()))