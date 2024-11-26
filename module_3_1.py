# Функция подсчета -
def count_calls():
    global calls  # Обьявление переменной глобального значения
    calls += 1


# Функция приема аргумента и возврата из него кортежа
def string_info(string):
    lenght = len(string)  # прием значения длины списка
    up_case_str = string.upper()  # прием в верхнем регистре
    low_case_str = string.lower()  # прием в нижнем регистре

    count_calls()  # использование первой функции
    return lenght, up_case_str, low_case_str  # возврат значений


# ФУнкция для проверки нахождения строки в списке
def is_contains(string, list_to_search):
    if string in list_to_search:  # оператор для проверки
        contains = True
    else:
        contains = False

    count_calls()  # Использование первой функции
    return contains


calls = 0  # Переменная подсчета вызовов функций



# тестовые значение для проверки
test_str = 'Arkady'
test_str_2 = 'MAximka'

# тестовые значение для проверки списка
test_list = ['Vovchik', 'Arkady', 'sveta']
test_list_2 = ['Chelyaba', 'RedHill','TUrbO']


# вызов функций для проверки
print(string_info(test_str))
print(string_info(test_str_2))
print(is_contains('Arkady', test_list))
print(is_contains('Moscow', test_list))
print(is_contains('chelyaba', test_list_2))
print(is_contains('DVs', test_list))

# фин результат
print(f'Функция была вызвана {calls} раз')
