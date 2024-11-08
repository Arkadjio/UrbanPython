# создаем класс
class House:
    # пустой список
    houses_history = []

    # метод нью
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # вызов метода супер-класса
        if len(args) > 0:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # текстовое представление сущности класса
    def __repr__(self):
        return f'House({self.name}, {self.number_of_floors})'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

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
h3 = House('ЖК Матрёшки', 20)

# Удаление объектов
del h2
del h3

print(House.houses_history)