    # Ставим обработку исключений
try:

    #Функция первая
    def square_number(num):
        return num/2
    # Ввод числа
    print("Введите число:")
    user_input = int(input())
    result = square_number(user_input)
    print(int(result))

    # Функция вторая
    def square_number_2(num):
        return num*4

    #Присвоение значения второй функции
    result_2 = square_number_2(result)
    print('Результат второй функии:-',end='')

    # Финальный вывод
    print(int(result_2))

except(ValueError, TypeError, ZeroDivisionError):
    if user_input == 0:
        print('Ошибка ввода  ')

# test-3
try:
    n = input("Enter a number: ")
    print(type(n))
    if n == str(n) or n == bool(n):
        n = float(n)
        print(type(n))
        print(n)

except(TypeError, ValueError, ZeroDivisionError):
        print("Please enter a number")
