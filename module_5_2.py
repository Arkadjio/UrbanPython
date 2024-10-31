# название и назнаяение класса
class House:
    # метод приема данных в класс
    def __init__(self, name, number_of_floors):
        # атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # метод для вывода этажей
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    # функция возврата этажей
    def __len__(self):
        return self.number_of_floors

    # функция возврата названия и кол-ва этажей
    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'


# назначение класса для переменной
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# проверка срабатывания меодов
h1.go_to(5)
h2.go_to(10)


# проверка срабатывания методов Module_5_2

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)


print(h3)
print(len(h3))
print(h4)
print(len(h4))
