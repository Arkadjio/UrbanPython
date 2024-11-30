
def add_everything_up(a, b):
    try:
        sum_numbers = a + b
        return sum_numbers
    except TypeError as exc_1:
        print(f'Ошибка:-разные типы данных- {exc_1}')
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
