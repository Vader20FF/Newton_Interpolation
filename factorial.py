def get_factorial(n):
    factorial_temp = 1
    if n in (0, 1):
        return 1
    else:
        for i in range(2, n+1):
            factorial_temp = factorial_temp * i
        return factorial_temp
