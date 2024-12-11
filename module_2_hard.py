# --- Функция для подбора пароля
def get_out(number):
    password = ''  # --- Пусстая строка
    for i in range(1, number):
        for j in range(2, number):

            if j <= i:  # --- Пропуск если меньше ---
                continue

            if number % (i + j) == 0:  # --- Проверка деления без остатка на заданное число ---
                password += str(i) + str(j)

    return password


# --- Задаем число ---
get_password = int(input('Enter an integer from 3 to 20: \n'))

# --- Пробуем ---
result = get_out(get_password)
print('Password:', result)

# ----- Сверка пароля  -----
list_pass = ''  # ----- Сюда вставить пасс который хотим проверить -----
print(result == list_pass)
