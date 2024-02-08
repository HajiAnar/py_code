def cache(func):
    results = {}

    def wrapper(*args):
        if args in results:
            return results[args]

        result = func(*args)
        results[args] = result
        return result

    return wrapper


@cache
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
