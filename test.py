def is_prime(func):
    def wrapper():
        prime = 0
        for i in range(2, func - 1):
            if func % i == 0:
                prime += 1
            if prime <= 0:
                return f'число {func} - простое!'
            else:
                return f'число {func} - составное!'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 4))
