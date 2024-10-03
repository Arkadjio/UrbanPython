# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# сортируем список для удобства
my_list.sort()

# делаем отсортированнный список в обратном порядке для удобства
my_list.reverse()
print(my_list)
# Начальное значение индекса
index = 0

# сам цикл
while index < len(my_list) and my_list[index] > 0:
    print(my_list[index])
    index += 1

# bitte