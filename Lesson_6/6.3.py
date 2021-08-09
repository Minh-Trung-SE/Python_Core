def is_perfect(number_check):
    check = 0
    if isinstance(number_check, int) and number_check > 0:
        for divisor in range(1, number_check):
            # If SUM() all of divisor which divisible == number
            # return true else false
            if number_check % divisor == 0:
                check += divisor
        if number_check == check:
            return True
        else:
            return False
    else:
        return False


number = int(input("Enter number to check it is perfect number: "))
print(f"{number} is perfect number: {is_perfect(number)}")
