# ----- Основная функция с перебором и назначением в словарь -----
def apply_all_func(int_list, *functions):
    results = {}  # ----- Пустой список -----
    for func in functions:
        func_name = func.__name__  # ----- Тут берем название функции -----
        func = func(int_list)  # ----- вызов всех функций из *functions -----
        results[func_name] = func  # ----- назначение ключа
    return results


# ----- Поехали -----
_list = [13, 2, 1, 4, 5, 713, 10]
result_1 = apply_all_func(_list, min, max)
result_2 = apply_all_func(_list, len, sum, sorted)
print(result_1)
print(result_2)
