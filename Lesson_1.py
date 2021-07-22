# init var name and input name
name = input("Enter Your Name: ")
# init var age and handle exception input if it occur
while True:
    try:
        age = int(input("Enter Your Birth Year: "))
        if age < 0 | age > 2021:
            print("Birth Year must be > 0 and <= 2021")
            continue
        else:
            break
    except ValueError:
        print("Invalid input!")
# display and calc age
print(f"Hello: {name}, Now you {2021 - age} year old!")
