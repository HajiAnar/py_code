def change(num):
    if num <= 0:
        return num
    change(num - 1)
    print(num)


number = int(input('Введите число: '))
change(number)

