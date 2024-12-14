# ---- класс исключения -----
class StepValueError(ValueError):
    pass


# ---- Класс итератор ----
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:  # ---- Создание исключения шага ------
            raise StepValueError("шаг не может быть равен - 0")
        self.start = start
        self.stop = stop
        self.pointer = self.start
        self.step = 1 if step > 0 else -1

    def __iter__(self):
        self.pointer = self.start  # ---- Указатель итерации в оснвоном равен точке отправления ----
        return self

    def __next__(self):
        if self.pointer * self.step >= self.stop * self.step:
            raise StopIteration  # ---- остановка итерации ----
        point = self.pointer  # ---- определение и возврат значения -----
        self.pointer += self.step
        return point


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
