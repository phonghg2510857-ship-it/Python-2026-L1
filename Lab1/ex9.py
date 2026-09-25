def factorial(n):
    if n < 0:
        raise('Error!')
    else:
        for i in range (1, n + 1):
            result *= i
        return result