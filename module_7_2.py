def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        string_positional = {}

        for i, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            string_positional[(i, position)] = string
        return string_positional


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
