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

# 6.7







