import os
import time

file_path = r'C:\Users\arkaa\PycharmProjects\pythonProject5\module_7'

print(os.getcwd())
print(os.listdir(file_path))

# метод walk
for root, directories, files in os.walk(file_path):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)

# метод join
print(os.path.join(file_path, 'module_7_5.py'))

# метод getmtime
last_time_modifield_file = os.path.getmtime(file_path)
print(last_time_modifield_file)
renable_last_time_modification = time.ctime(last_time_modifield_file)
print(f'Последнее изменение былло: {renable_last_time_modification}')

# получение размера ффайла - в байтах
size_file = os.path.getsize(file_path)
print(size_file)

# получение родительской папки
file_dirname = os.path.dirname(file_path)
print(file_dirname)



