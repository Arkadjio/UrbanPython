import string


class WordsFinder:

    def __init__(self, *file_names):  # инит с неограничнным приемом значений
        self.file_names = file_names

    # подготовительный метод возврата словаря
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, 'r', encoding='utf-8') as f):
                words = f.read().lower()  # перевод в нижний регистр
                str_pnk = str.maketrans(',', ',', string.punctuation + '-')  # избавление от знаков пуктуации
                words = words.translate(str_pnk)  # перевод мэйктранс
                words = words.split()  # разделение слов
                all_words[file_name] = words
                return all_words

    # метод поиска слов
    def find(self, word):
        all_words = self.get_all_words()  # назначение метода get_words
        result = {}  # словарь для возврата
        word = word.lower()  # перевод в нижний регистр
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
            return word, result

    # метод кол-ва слов
    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.count(word)
            return result


# прроверка методов
if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
