def min_divider(n, d=2):
    return d if n % d == 0 else min_divider(n, d + 1)
number = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы: ', min_divider(number))