from functools import wraps
from typing import Callable, Optional, Any


def decorator_with_args_for_any_decorator(enhance_func: Callable) -> Callable:
    """Декоратор, который дает возможность другому декоратору принимать производные аргументы"""
    def maker(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return enhance_func(func, *args, **kwargs)

        return wrapper

    return maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """Декоратор . Шаблон"""
    @wraps(func)
    def wrapper(func_args: Optional[Any], func_kwargs: Optional[Any]) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        result = func(func_args, func_kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей', 4564564, test_01=34, test_02='аргумент my_str')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
decorated_function("Юзер", 101)
