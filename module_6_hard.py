class Figure:
    """Родительский класс"""

    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    @staticmethod
    def __is_valid_color(r, g, b):
        for c in [r, g, b]:
            if isinstance(c, int) and 0 <= c <= 255:
                return True
            return False

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int) and side > 0:
                    return True
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length):
        super().__init__(color, length)
        self.__radius = length / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        sides = [edge] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
