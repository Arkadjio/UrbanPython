from random import randint as ran


# Родителский класс
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    # методы
    def move(self, dx, dy, dz):
        if dz < 0 and self._cords[2] + self.speed * dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz

    def get_cords(self):
        print('x =' + str(self._cords[0]), 'y =' + str(self._cords[1]), 'z =' + str(self._cords[2]))

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('''Sorry, i'm peaceful :''')
        else:
            print('''Be careful, i'm attacking you 0_0''')

    def speak(self):
        if self.sound is not None:
            print(self.sound)


# доп классыв
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print('Here are(is)', ran(1, 4), 'eggs for you')


class Aquatic_Animals(Animal):
    _DEGREE_OF_DANGER = 3.

    def dive_in(self, dz):
        self._cords[2] -= self.speed * abs(dz) / 2


class Poison_Animal(Animal):
    _DEGREE_OF_DANGER = 8


# Утконос и его унаследованные методы
class Duckbill(Poison_Animal, Aquatic_Animals, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        super().lay_eggs()

    def dive_in(self, dz):
        super().dive_in(dz)

    def speak(self):
        super().speak()

    def attack(self):
        super().attack()


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
