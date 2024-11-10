# Родительский класс - Животное
class Animal:
    alive = True
    fed = False

    # инит
    def __init__(self, name):
        self.name = name

        def eat(self, food):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False


# Родительский класс - Растение
class Plant:
    edible = False

    # инит
    def __init__(self, name):
        self.name = name


# класс - Фрукт
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # переопределяем значение(сьедобное)
        self.edible = True


# класс - Цветок
class Flower(Plant):
    pass


# класс - Млекопитающеее
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


# класс - Хищник
class Predator(Mammal):  # Я отнес класс хищников к млекопитающим потому,хищник это тоже млекопитающее
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
