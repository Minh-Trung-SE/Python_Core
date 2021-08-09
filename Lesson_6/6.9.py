def count_digitos_impares(n):
    count = 1
    if n == 0:
        return 0
    elif (n % 10) % 2 == 0:
        return count_digitos_impares(n // 10)
    elif (n % 10) % 2 == 1:
        return count + count_digitos_impares(n // 10)
