def is_prime(func):
    # ---- внутреняя функция wrapper -----
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        sum_ = sum(args)  # ----сцмма переданных аргументов -----
        count_num = 0  # ---- счетчик для поиска делителей  -----

        # ---- перебор числа на поиск делителей  ----
        for i in range(2, sum_ // 2 + 1):  # ---- диапозон от 2 до корня суммы переданных аргументов -----
            if sum_ % i == 0:
                count_num = count_num + 1  # ---- передача в счетчик -----

        # ---- основная проверка ----
        if count_num <= 0:
            print('Простое')
        else:
            print('Составное')

        return result

    return wrapper


# ---- основная функция ----
@is_prime  # ---- назначение декоратора ----
def sum_three(*args):
    return sum(args)


# ----  проверка работоспособности ----
print(sum_three(2, 5, 4))
