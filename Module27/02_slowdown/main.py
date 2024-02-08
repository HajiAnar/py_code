import time
import requests
from typing import Callable
import functools

def slow_down(func) -> Callable:
    """Декоратор, обеспечивающий задержку функции, которая проверяет изменения данных на веб-странице или её кода."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(5)
        value = func(*args, **kwargs)
        end = time.time()
        print('Команда выполнена за {} секунд.'.format(end - start))
        return value

    return wrapper


@slow_down
def get_webpage(page: str) -> str:
    """Функция, которая проверяет изменения данных на веб-странице или её кода."""

    response: requests
    print(f'Получение данных со страницы: {page}')
    try:
        response = requests.get(page, timeout=5)
        print('Данные успешно получены')
        result = response.text
        response.close()
    except requests.exceptions.RequestException as err:
        result = err
    return result


page_one = get_webpage('https://mail.ru')
page_two = get_webpage('https://google.com')
