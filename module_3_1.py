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
    list_to_search = [element.lower() for element in list_to_search]
    if string.lower() in list_to_search:  # оператор для проверки
        contains = True
    else:
        contains = False

    count_calls()  # Использование первой функции
    return contains


calls = 0  # Переменная подсчета вызовов функций

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
# фин результат
print(f'Функция была вызвана {calls} раз')
