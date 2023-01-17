def factorial_res(n):
    if n <= 1:
        return 1
    return n*factorial_res(n-1)
factorial_res(5)