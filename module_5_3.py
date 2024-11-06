# создаем класс
class House:
    # инициализация
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # текстовое представление сущности класса
    def __repr__(self):
        return f'House({self.name}, {self.number_of_floors})'

    # сравнение этажей у селф и азер
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            raise TypeError("обьекты разных типов")

    # больше - меньше
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            raise TypeError("обьекты разных типов")

    # больше меньше равно
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            raise TypeError("обьекты разных типов")

    # то же самое больше меньше
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            raise TypeError("обьекты разных типов")

    # то же самое больше меньше равно
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            raise TypeError("обьекты разных типов")

    # проверка на неравнество
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            raise TypeError("обьекты разных типов")

    # добавление знаечения
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            raise TypeError("обьекты разных типов")

    # тоже самое длоавление значений
    def __iadd__(self, value):
        return self.__add__(value)

    # тоже самое длоавление значений
    def __radd__(self, value):
        return self.__add__(value)


# Создаем два объекта класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)

print(h1 == h2)
h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__

print(h1 >= h2)  # __ge__

print(h1 < h2)  # __lt__

print(h1 <= h2)  # __le__

print(h1 != h2)  # __ne__
