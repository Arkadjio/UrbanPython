from itertools import combinations  # --- импорт комбинаций ---


def all_variants(text):
    len_txt = len(text)
    for x in range(1, len_txt + 1):  # --- начало с одного так,как ниже вставка джоин ---
        for z in combinations(text, x):
            yield ''.join(z)  # --- обьединяем строки ---


# --- проверка ---
a = all_variants("abc")
for i in a:
    print(i)
