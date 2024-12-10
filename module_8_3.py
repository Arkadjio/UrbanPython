class IncorrectVinNumber(Exception):
    """Исключение неправильного Vin номера"""

    def __init__(self, message='Некорректный вин номер'):
        self.message = message


class IncorrectCarNumbers(Exception):
    """Исключение неправильных номеров машин"""

    def __init__(self, message='Некорректный номер машины'):
        self.message = message


class Car:
    """Класс машин"""

    def __init__(self, model: str, vin: int, numbers: str):  # ---Заранее определяем тип аргументов
        self.model = model
        self.__vin = vin
        self.__is_valid_vin(vin)  # -- метод проверки корректности вин кода
        self.__numbers = numbers
        self.__is_valid_numbers(numbers)  # -- метод проверки корректности номера автоЧ

    def __is_valid_vin(self, vin_number):  # -- метод проверки корректности вин кода
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif len(str(vin_number)) != 7:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):  # -- метод проверки корректности номера авто
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


# -------First-------
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

# -------Second-------
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

# --------Third-------
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')


