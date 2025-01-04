# ----- импорт необходимых библиотек -----
import datetime
import multiprocessing as mp


# ----- функция для считывания и добавления значений в список -----
def read_info(name):
    all_data = []
    # ----- конструктор для открытия файлоа -----
    with open(name, 'r') as f:
        for line in f:  # ----- перебор строк для добавления в список all_data -----
            f.readline().strip('')  # ----- readline по условию -----
            all_data.append(line)  # ----- добавление в список -----


# ----- необходимый конструктор для работы с mp -----
if __name__ == '__main__':

    # ----- линеное открытие файлов -----
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.datetime.now()  # ----- начало работы линейного вызова -----

    # ----- перебор названий файлов и их назначение в функцию -----
    for i in filenames:
        read_info(i)

    print(datetime.datetime.now() - start_time, 'линейный')  # ----- подсчет времени ------

    # ----- подсчет времени для mp ------
    start_time_2 = datetime.datetime.now()

    a = len(filenames)  # ----- на тот случай если не значем сколько файлов в директории -----

    # ----- конструктор мп ------
    with mp.Pool(processes=a) as pool:
        pool.map(read_info, filenames)

    stop_time_2 = datetime.datetime.now()
    print(stop_time_2 - start_time_2, 'многопроцессный ')
