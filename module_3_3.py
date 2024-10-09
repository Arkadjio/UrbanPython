#создаем функциж
def print_params(a=1, b='string',c =True):
    print(a,b,c)

#проверка работы функции
print_params(a= 2, b = 42, c= False)
print_params(3,int)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

#Подготовка к распаковке параметров

#список с тремя значениями разных типов
values_list = ['строка', False, 5]
#словарь с тремя ключами
values_dict = {'a': True, 'b': (3,3,3), 'c': [1, 2, 3]}
#список с двумя значениями разных типов
values_list_2 = [bool, (1,2,3)]

#проверка распаковки списка
print_params(*values_list)
#проверка распаковки словаря
print_params(**values_dict)
#проверка распаковки словаря с двумя элементами разных типов
print_params(*values_list_2,42)

