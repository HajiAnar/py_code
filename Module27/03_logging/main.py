from datetime import datetime
import functools


def logging(func):
    """Декоратор, отвечающий за логгирование функций"""
    @functools.wraps(func)
    def wrapper():
        try:
            print(f'{func.__name__} - {func.__doc__}')
            func()
        except Exception as e:
            e = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {func.__name__} - {e}\n'
            with open('function_error.log', 'a+', encoding='utf-8') as f:
                f.write(e)
            print(e)

    return wrapper

@logging
def zerodiv() -> None:
    """Деление на ноль"""
    x = 1 / 0


@logging
def varname() -> None:
    """Присвоим не существующую переменную"""
    x = y


@logging
def just() -> None:
    """Присваение переменной значения"""
    x = 'Hello World!!!'

zerodiv()
varname()
just()