
def summ(n):

    num_sum = 0

    while n != 0:
        last_num = n % 10
        num_sum += last_num
        n //= 10

    print('', num_sum)
    return num_sum

def count_n(n):

    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

number = int(input('Введите число: '))

sums = summ(number)
counts = count_n(number)

print('\nСумма чисел:', sums)
print("\nКоличество цифр в числе: ", counts)

print('\nРазность суммы и количества цифр:', sums - counts)
