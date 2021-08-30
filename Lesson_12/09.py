def extract_characters(file_input):
    return {char for char in file_input.read()}


file = open('07.txt', mode='r', encoding='utf8')
print(extract_characters(file))
