

# Здесь создайте функцию get_sage_sqrt
import math

def get_sage_sqrt(n):
    try:
        return math.sqrt(n)
    except ValueError as exc:
        if exc.args[0] == 'math domain error':

            return None
    else:

        raise exc

    n = float(input("Введите число: "))
    result = get_sage_sqrt(n)

    if result is None:
        print("Ошибка при вычислении квадратного корня.")
    else:
        print(f"Квадратный корень из числа {n} равен {result}.")


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")