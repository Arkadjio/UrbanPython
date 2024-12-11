from random import choice

# ----- строки для работы -----
first = 'Мама мыла раму'
second = 'Рамена мало было'

# ----- Создание лямбда функции -----
first_result = list(map(lambda x, y: x == y, first, second))
print(first_result)


# ----- создание замыкания -----
def get_advanced_writer(file_name):
    def write_everything(*data_set):  # ---создание функции открытия и добавления элементов дата-сэт ---
        with open(file_name, 'a', encoding='utf-8') as file:  # --- аппэнд для записи и перекодировка ---

            for data in data_set:
                file.write(str(data))  # --- вывод в строковый тип, без него дата-сэт не берет списки
                file.write('\n')

    return write_everything


# ----- Пробуем -----
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# ---- Создание класса -----
class MysticBall:
    def __init__(self, *words):  # ---- *
        self.words = list(words)

    def __call__(self):  # --- метод возврата случайного слова ----
        if len(self.words) == 0:
            raise IndexError('Сир! В коллекции ничего не найдено!')  # --- небольшое исключение ----
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
