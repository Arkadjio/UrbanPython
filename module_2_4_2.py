# начальный список всех чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#  список в который будем добавлять только простые числа
primes = []

#список в который будем добавлять составные числаe
not_primes = []

# упреждение на единицу
for number in numbers:
    if number == 1: # пропускаем 1 так , как 1 не составноеи не простое
        continue

    is_prime = all(number % i != 0 for i in range(2, number)) # вложенный цикл исключения попадания 1 в списки
    prime_list = primes if is_prime else not_primes
    prime_list.append(number)


# финальный вывод на консоль
print(f'список простых чисел \n {primes}')
print(f'список составных чисел \n {not_primes}')
