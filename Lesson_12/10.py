import os
import string
if not os.path.exists("letters"):
    os.makedirs("letters")

for letter in string.ascii_uppercase:
    open('letters/' + letter + ".txt", "a").close()