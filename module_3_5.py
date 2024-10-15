# создаем функцию
def get_multiplied_digits(number):
    # переменная со строковым значением аргумента
    str_number = str(number)

    # возврат первого символа с типом цулое число
    first = int(str_number[0])

    # услов.оператор на проверку работоспособности
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


# проверка результата
result = get_multiplied_digits(40203)
print(result)
