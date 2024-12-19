# ----- создаем функцию - генератор -----
def all_variants(text):
    for letter in range(len(text)):  # ----- первый перебор -----
        for var in range(len(text) - letter):  # ----- второй перебор -----
            yield text[var:var + letter + 1]  # ----- возврат ------


# ----- проверка -----
a = all_variants('abc')
for i in a:
    print(i)
