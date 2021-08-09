def change_upper_lower(msg):
    new_str = ""
    for i in range(len(msg)):
        if msg[i].isupper():
            new_str += msg[i].lower()
        elif msg[i].islower():
            new_str += msg[i].upper()
        else:
            new_str += msg[i]
    return new_str