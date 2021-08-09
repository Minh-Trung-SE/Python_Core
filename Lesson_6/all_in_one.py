# 6.1 exercise // find max and min in *number
def max_min(*numbers):
   return max(numbers), min(numbers)

# 6.2 exercise // converting a string to reverse
def reverse_string(msg):
    result = msg[::-1]
    return result

# 6.3 exercise // cheking perfect_number
def is_perfect(number):
    check = 0
    if isinstance(number, int) and number > 0:
        for divisor in range(1, number):
            # If SUM() all of divisor which divisible == number
            # return true else false
            if (number % divisor == 0):
                check += divisor
        if number == check :
            return True
        else:
            return False
    else:
        return False

# 6.4 exercise // checking prime
def is_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

# 6.5 exercise //
def count_upper_lower(msg):
    upper = [check for check in msg if check.isupper()]
    lower = [check for check in msg if check.islower()]
    return len(upper), len(lower)

# 6.6 exercise //
def is_pangram(msg, alphabet):
    return not set(alphabet) - set(msg.lower())

# 6.7 App BMI
def bmi_calculator(weight, height):
    result_bmi = weight/(height*2)
    return result_bmi

def bmi_infor(weight, height):
    bmi = bmi_calculator(weight, height)
    if bmi < 18.5:
        print("UNDERWEIGHT")
    if bmi >= 18.5 and bmi <= 24.9:
        print("NORMAL")
    if bmi >= 25 and bmi <=29.9:
        print("OVERWEIGHT")
    if bmi >= 30 and bmi<=34.9:
        print("OBESE")
    if bmi > 35:
        print("EXTREMLY OBESE")

# 6.8 exercise
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

# 6.9 exercise
def count_digitos_impares(n):
    count = 1
    if n == 0:
        return 0
    elif (n%10)%2 == 0:
        return count_digitos_impares(n//10)
    elif (n%10)%2 == 1:
        return count + count_digitos_impares(n//10)

# 6.10 exercise fibonacci
def recur_fibo(n):
    if n <= 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
# 6.11 exercise // method: getting a positive integer from the user and checking validations
def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")

# 6.13 exercise // find x in source

# Dear instructor >> it's not necessary to built a new method while Python had this :)))

# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)









