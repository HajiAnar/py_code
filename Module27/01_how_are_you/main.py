import functools
from typing import Callable

def how_are_you(func: Callable) -> Callable:
    """Декоратор, который при вызове функции интересуется делами пользователя"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input('Привет, как дела?  ')
        print('А у меня не очень... Ладно, держи свою функцию')
        result = func(*args, **kwargs)
        return result

    return wrapper

@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()