while True:
    try:
        age = int(input("Enter your age: "))
        income = float(input("Enter your income: "))
        if age >= 0 and income >= 0 :
            break
    except ValueError:
        print("Invalid value")

if age >= 18 and income >= 2500:
    print("Congratulations you are enough condition to borrow money! ")
else:
    print("Sorry! You not enough condition to borrow money")