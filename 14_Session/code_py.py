
# find factrorial 


def find_factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * find_factorial(n-1)


factorial = find_factorial(4)
print(factorial)