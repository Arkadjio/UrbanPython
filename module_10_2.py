import threading
import time


class Knight(threading.Thread):
    opponent = 100
    day_combat = 0

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали !')
        self.combat()
        print(f'{self.name} одержал победу спустя {self.day_combat}')

    def combat(self):
        while self.opponent != 0:
            time.sleep(1)
            print(f'{self.name} сражается {self.day_combat}...осталось {self.opponent} воинов')
            self.day_combat += 1
            self.opponent -= self.power


# Создание класса
# first_knight = Knight('Sir Lancelot', 10)
# second_knight = Knight("Sir Galahad", 20)
#
# first_knight.start()
# second_knight.start()

knight_wife = Knight('Sir.Valeriks', 25)
knight_wife.start()
