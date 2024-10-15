# функция для поиска однокоренных слов
def single_root_words(root_word, *other_words):
    same_words = []  # пустой список для однокоренных слов

    # преобразуем список с проверяемыми словами в ниж.рег
    other_words = (other_words.lower() for other_words in other_words)
    # преобразуем первый аргумент функции сразу в нижний регистр
    root_word = root_word.lower()
    # цикл перебора слов
    for i in other_words:
        if i.lower() in root_word or root_word in i:
            same_words.append(i)
    return same_words  # возврат списка


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
