import random
"""Exception - Базовый класс исключений"""

class KillError(Exception):

    def __init__(self):
        super().__init__('Убийство, сэр!')
"""Класс KillError возвращает str"""

class DrunkError(Exception):
    def __init__(self):
        super().__init__('Вы опять надрались, сэр!')
"""Класс DrunkError возвращает str"""

class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Авария на дороге!')
"""Класс CarCrashError возвращает str"""


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Наелся булок')
"""Класс GluttonyError возвращает str"""

class DepressionError(Exception):
    def __init__(self):
        super().__init__('Впал в беспросветную депрессию')
"""Класс DepressionError возвращает str"""

class Buddhist:
    def __init__(self, karma = 0):
        self.karma = karma

    """Класс Буддист
     Arg:
     karma(int) - общее количество пунктов кармы """
    def set_karma(self, karma):
        self.karma += karma
    """Сеттер для получения пунктов кармы
    :param karma: карма
    :type: int"""
    def get_karma(self):
        return self.karma
    """Геттер для получения кармы
    :return  karma
    :rtype int"""


def one_day():

    choice = random.randint(1, 10)
    if choice == 1:
        try:
            exception = random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))
            raise exception()

        except Exception as exc:

            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'День: {day} Исключение: {exc}\n')
                file.close()
    else:
        return random.randint(1, 7)

"""Функция для получения пунктов кармы за один день. С вероятность 1 к 10 выкидывает исключение и записывает его в файл karma.log. 
Иначе возвращает пункты кармы от 1 до 7 """


buddhist = Buddhist()
day = 0
while buddhist.get_karma() < 500:
    day += 1
    result = one_day()
    if not isinstance(result, int):
        pass
    else:
        buddhist.set_karma(result)



print(('Просветление достигнуто. Количество дней', day))
