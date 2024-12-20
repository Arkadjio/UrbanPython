# ----- Импорты необходимых модулей и функций -----
import threading
import time


# ----- Объявление функции write_words -----
def write_words(word_count, file_name):
    try:
        # ----- блок на запись в файлы -----
        with open(file_name, 'w', encoding='utf-8') as f:
            for word in range(1, word_count + 1):
                some_word = f'Какое-то слово № {word}\n'
                f.write(some_word)
                time.sleep(0.1)  # ----- пауза -----
        print(f'Завершилась запись в файл {f.name}')
    except Exception as exc:
        print(f'Ошибка записи в файл - {exc}')


# ----- Взятие текущего времени -----
start_time = time.time()

# ----- Запуск функций с аргументами из задачи -----
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# ----- Взятие текущего времени -----
stop_time = time.time()

# ----- Вывод разницы начала и конца работы функций -----
time_differences = stop_time - start_time
print(f'Последовательная запись заняла:{time_differences} секунд')

# ----- Взятие текущего времени -----
start_time_thread = time.time()

# ----- Создание и запуск потоков с аргументами из задачи -----
threads = []
for i in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=i)
    threads.append(thread)
    thread.start()

# ----- остановка основного потока -----
for j in threads:
    j.join()

# ----- Взятие текущего времени -----
stop_time_threads = time.time()

# ----- Вывод разницы начала и конца работы потоков -----
time_differences_thread = stop_time_threads - start_time_thread
print(f'Параллельная запись в файлы заняла: {time_differences_thread} секунд')
