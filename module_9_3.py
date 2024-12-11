# -----  Списки для работы -----
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# ----- первый генератор -----
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

# ----- второй генератор -----
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))

# ----- он же второй но с использованием зипа -----
second_result_2 = (len(x) == len(y) for x, y in zip(first, second))
print(list(second_result_2))

