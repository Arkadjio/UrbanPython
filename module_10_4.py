# ---- импорт всего необзодимого
from threading import Thread
from time import sleep
from random import randint
from queue import Queue


# ---- создаем класс на столы ----
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


# ---- класс гостей наследуемый от класса трэд ----
class Guest(Thread):
    # ---- перенаследуем класс и методы ----
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    # ---- перенаследуем ран ----
    def run(self):
        sleep(randint(3, 11))


class Cafe:  # ---- класс кафе ----
    # ----
    def __init__(self, *tables):
        self.tables = list(tables)  # ---- неограниченное колво столов ----
        self.queue = Queue()  # ---- очередь ----

    # ---- прибытие гостей ----
    def guest_arrival(self, *guests):
        # ---- дадим перебор на проверку ----
        for guest in guests:
            # ----  проверка на свободный стол ----
            if any(table.guest is None for table in self.tables):  # ---- эни тру если бул значение в итерируем обт. тру

                free_table = next((table for table in self.tables if table.guest is None), None)  # на некст ctrl пикаем
                free_table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
                guest.start()  # ---- запуск потока ----
            else:
                self.queue.put(guest)  # ---- зкаидываем в очередь ----
                print(f"{guest.name} в очереди")

    # ---- процесс обслуживания гостей ----
    def discuss_guests(self):
        # ---- пока очередь не пустая или столы не пустуют ----
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            # ---- перебор столов ----
            for table in self.tables:
                # ---- проверка на свободный стол и рабочий поток ----
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

            # ---- тут сажаем гостей за стол если он свободен -----
            if not self.queue.empty():
                # ---- перебор свободных столов ----
                for table in self.tables:

                    if table.guest is None:
                        new_guest = self.queue.get()  # ---- вытаскиваем из очереди ----
                        table.guest = new_guest
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        new_guest.start()
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
