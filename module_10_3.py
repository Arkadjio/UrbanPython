# -----  импорт библиотек -----
from threading import Thread, Lock
import time
from random import randint


# ----- создаане класса для дальнейшей работы -----
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()  # ----- обьект класса Лок ------

    # ----- функция на пополнение случайным числом 100 раз # -----
    def deposit(self):
        # ----- запуск на 100 раз -----
        for i in range(100):
            money = randint(50, 500)  # ----- переменная для рандомного числа -----
            # ----- работаем с виз потому что так легче и меньше писать -----
            self.balance += money
            # ----- проверка баланса ----
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f'Пополнение:{money}, Баланс:{self.balance}')  # ----- вывод текущего баланса -----
            time.sleep(0.001)  # ----- тут можно поставить свое значение -----

    # ----- метод вывода денег -----
    def take(self):
        # ----- так же 100 раз -----
        for i in range(100):
            withdraw_money = randint(50, 500)
            # ----- так же работаем с виз ------
            with self.lock:
                print(f'Запрос на {withdraw_money}')

                # ----- блок проверки значения случайного числа -----
                if withdraw_money <= self.balance:
                    self.balance -= withdraw_money
                    print(f'Снятие: {withdraw_money}. Баланс: {self.balance}.')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    self.lock.acquire()


# ----- Проверка -----
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
