def get_int(prompt):
    int_number = 0
    while True:
        try:
            int_number = int(input(prompt))
            break
        except ValueError:
            print("Not valid int number!")
    return int_number


n = get_int("Enter N: ")
sum_of_digital = 0
while True:
    if n >= 1000 or n <= 0:
        print("You must enter positive number")
        n = get_int("Enter N: ")
    else:
        break
while n > 0:
    sum_of_digital += n % 10
    n = n // 10

print(sum_of_digital)
