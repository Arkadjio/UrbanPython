# функция для перебора и возврата
def calculate_structure_sum(*args):
    # пустой список для добавления
    result_sum = 0

    for i in args:
        if isinstance(i, int):
            result_sum += i
        elif isinstance(i, str):
            result_sum += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(value, int):
                    result_sum += value
                if isinstance(value, str):
                    result_sum += len(value)
                if isinstance(key, str):
                    result_sum += len(key)
                if isinstance(key, int):
                    result_sum += key
        else:
            # Рекурсивный вызов
            result_sum += calculate_structure_sum(*i)
    return result_sum


# Условный список
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])

]

# переменная для вызова функции
result = calculate_structure_sum(*data_structure)
print(result)  # Вывод 99
