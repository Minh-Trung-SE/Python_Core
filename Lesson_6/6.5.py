def count_upper_lower(msg):
    upper = [check for check in msg if check.isupper()]
    lower = [check for check in msg if check.islower()]
    return len(upper), len(lower)