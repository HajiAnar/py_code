



print('Введите числа через пробел: ')
numbers = [int(number) for number in input().split()]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')