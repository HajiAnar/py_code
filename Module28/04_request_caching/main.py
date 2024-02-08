from collections import OrderedDict
from typing import Union


class LRUCache:
    """ Класс хранит ограниченное количество объектов и если лимит превышен,
        удаляются самые старые использованные элементы. """

    def __init__(self, capacity: int) -> None:
        """ Конструктор для инициализации атрибутов класса.

        Args:
            capacity (int): Максимальное количество объектов, которые можно хранить в кэше.
        """
        self.__capacity = capacity
        self.__cache_dict = OrderedDict()

    @property
    def cache(self) -> Union[tuple, str]:
        """ Возвращает последнюю пару ключ-значение из словаря __cache_dict.
            Если словарь пуст, возвращает строку 'Элементов в кэше нет'.

        Returns:
            Последняя пара ключ-значение из словаря __cache_dict, если словарь не пуст.
            Если словарь пуст, возвращает строку 'Элементов в кэше нет'.
        """
        return next(iter(self.__cache_dict.items())) if self.__cache_dict else 'Элементов в кэше нет'

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """ Добавляет в кэш новый элемент, предварительно производит проверку на переполнение. """
        if len(self.__cache_dict) >= self.__capacity:
            self.__cache_dict.popitem(last=False)
        self.__cache_dict[new_elem[0]] = new_elem[1]

    def print_cache(self) -> None:
        """ Выводит текущий кэш. """
        print('LRU Cache:')
        if self.__cache_dict:
            for key, value in self.__cache_dict.items():
                print(f'{key} : {value}')
        else:
            print('Элементов в кэше нет')

    def get(self, key: str) -> str:
        """ Возвращает значение искомого ключа в словаре.

        Returns:
            Значение ключа из словаря __cache_dict если такое имеется.
            Если такого ключа нет, возвращает строку 'Такого значения не существует'.
        """
        if key in self.__cache_dict:
            self.__cache_dict.move_to_end(key)
            return self.__cache_dict.get(key)
        else:
            return 'Такого значения не существует'


# cache = LRUCache(3)
#
# cache.cache = ('key1', 'value1')
# cache.cache = ('key2', 'value2')
# cache.cache = ('key3', 'value3')
#
# cache.print_cache()
#
# print(cache.get('key2'))
#
# cache.cache = ('key4', 'value4')
#
# cache.print_cache()



# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4