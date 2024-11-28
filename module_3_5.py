# создаем функцию
def get_multiplied_digits(number):
    str_number = str(number)  # даес строковое представление
    first = int(str_number[0])  # первое число

    if len(str_number) > 1: # создаем условие для рекурсии
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1: # страховка на тот случай если последнее число - 0
        first = 1
        return first


# проверка результата
result = get_multiplied_digits(1230200)
print(result)
