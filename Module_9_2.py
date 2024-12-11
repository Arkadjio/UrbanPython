# ----- Списки -----
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# ----- Создаем список из длин строк списка first_strinf -----
first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

# ----- список из пар слов (кортежей) одинаковой длины -----
second_result = [(x, y) for x in second_strings for y in first_strings if len(x) == len(y)]
print(second_result)

# ----- Словарь-- key-value: string-len -----

general_list = first_strings + second_strings
third_result = {x: len(x) for x in general_list if len(x) % 2 == 0}
print(third_result)


