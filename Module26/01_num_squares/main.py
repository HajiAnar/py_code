from typing import Iterable

# генераторное выражение
number: int = int(input('Введите число: '))
square_gen = (numb ** 2 for numb in range(1, number + 1))

print("Результат генераторного выражения")
for i_numb in square_gen:
    print(i_numb, end=' ')
print()

def square_gen(num: int) -> Iterable[int]:
    """Функция-генератор принимает число от пользователя и возвращает квадраты чисел от еденицы до вход.числа"""
    for num in range(1, num + 1):
        yield num ** 2

number:int = int(input('Введите число: '))
print("Результат функции-генератора")
for value in square_gen(number):
    print(value, end=' ')

print()

# класс-итератор
class SquareNum:
    """Класс SquareNum
    Атрибуты:
    count - счетчик
    number - int - число"""
    def __init__(self, number: int) -> None:
        self.count = 0
        self.number = number


    def __iter__(self):
        """Метод-итератор
        возвращает self"""
        return self


    def __next__(self)  -> int:
        """ метод, который возвращает очередное значение - int"""
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        else:
            return self.count ** 2

user_number = int(input('Введите число: '))
my_iter = SquareNum(user_number)
print("Результат класса-итератора")
for value in my_iter:
    print(value, end=' ')
