# -- функция возврата суммы чисел и некоректных значений
def personal_sum(numbers):
    result = 0  # -- сумма чисел
    incorrect_data = 0  # -- кол-во некоректных значений

    for number in numbers:  # -- перебор значений
        try:
            result += number
        except TypeError:  # -- обработка исключения ошибки типа
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    return result, incorrect_data


# -- функция подсчета среднего арифметического
def calculate_average(numbers):
    try:
        if isinstance(numbers, (list, tuple, set, str)):
            try:
                sum_of_numbers, incorrect_data = personal_sum(numbers)  # -- передача значений результ и инкоррект_дата
                average = sum_of_numbers / (len(numbers) - incorrect_data)  # -- основное вычисление
                return average
            except ZeroDivisionError:  # -- обработка исключения деления на ноль
                return 0
    except TypeError:  # -- обработка исключения ошибки типа
        print('В numbers записан некорректный тип данных')
        return None


# -- ПОЕХАЛИИИ
if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
