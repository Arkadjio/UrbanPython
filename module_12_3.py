import inspect
import types
from pprint import pprint as pp


def introspection_info(obj):
    full_info = {}

    full_info['Тип объекта - '] = type(obj)

    obj_attr = []
    obj_meth = []

    for _ in dir(obj):
        if not _.startswith('__'):
            val = getattr(obj, _)
            if isinstance(val, (types.MethodType, types.FunctionType)):
                obj_meth.append(_)
            else:
                obj_attr.append((_, repr(val)))

    full_info['Атрибуты - '] = obj_attr
    full_info['Методы - '] = obj_meth

    module_obj = inspect.getmodule(type(obj))
    if module_obj is not None:
        full_info['Модуль'] = module_obj.__name__

    if inspect.isroutine(obj):
        full_info['Аргументы функции -'] = inspect.signature(obj)

    return full_info


# ---- Подготовка к проверке ----

class Graphic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def some_kind_method(self):
        pass


example_cls = Graphic(3, 4)


def sum_num(x, y):
    return x + y


check_info_cls = introspection_info(example_cls)
pp(check_info_cls)

pp(introspection_info(inspect))

pp(introspection_info(sum_num(3,5)))
