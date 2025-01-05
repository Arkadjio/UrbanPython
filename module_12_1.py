import requests as req
import pprint as p
import pandas as pd
import numpy as np

'''тут про REQUESTS'''

google = req.get('https://www.google.com/search?q=')  # ----- поисковик ----
print(google.status_code)  # ----  должен показать трехзначное число , значения кодов состояния запроса http -->
# 1xx - информационные
# 2xx - успешные
# 3xx - перенаправление
# 4xx -клиентские ошибки
# 5xx - серверная ошибка

if google.ok:
    print('успешное подключение для пользователя ')  # ----  метод ок возвращает тру если статус-код  меньше 400

# -----  бывает что ответ приходит в виде типа -json- -----
# ----- для этого и пользуемся методом -json- -----

json_object = req.get('https://api.github.com')
print(json_object.status_code)
if json_object.ok:
    print('успешное подключение для пользователя ')

# json_object = json_object.json() # -----  и сам метод json -----
# p.pprint(json_object)  # -----  теперь когда распарсили используем на свое усмотрение -----


print(json_object.headers)
print(json_object.request.headers)

''' тут про pandas м нампи  '''
data = ['Pandas', 'Matplotlib', 'Numpy']  # ----- сериес файлы ----- только мндекс и его файлы ------
s = pd.Series(data)
print(s)

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print(s)

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])  # ----- рандомное заполнение индексов -----
print(s)

print(s.index)

''' и так до самого конца '''
