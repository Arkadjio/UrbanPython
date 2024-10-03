# начальный список всех чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'начальный список {numbers}')

# список в который будем добавлять только простые числа
primes = []

#  список в который будем добавлять составные числа
not_primes = []

# уппреждение на единицу
for number in numbers:
    if number == 1:
        continue  # пропускаем 1 так , как 1 не составноеи не простое

    is_prime = True

    # влооженный цикл  -  исключение попадания 1 в списки
    for i in range(2, number):
        if number % i == 0:  # проверка делимости
            is_prime = False
            break  # конец цикла при проверке

    #  распределяем числа по спискам
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# финальный вывод на консоль
print(f' ---список простых чисел--- \n {primes}')
print(f'---список составных чисел--- \n {not_primes}')
