import random

numb_sum = 0
lucky_numb = 777

with open ('out_file.txt', 'w') as numbers_file:

    while numb_sum <= lucky_numb:
        try:
            number = int(input('Введите число: '))
            numb_sum += number

            if 13 == random.randint(1, 13):
                raise Exception


            numbers_file.write(str(number) + '\n')

        except Exception:
            print("Вас постигла неудача!")
            break



    print('Вы успешно выполнили условие для выхода из порочного цикла!\n')


print('Содержимое файла out_file.txt')
with open('out_file.txt', 'r', encoding='utf-8') as final_file:
    lines = final_file.readlines()
    for line in lines:
        print(line)
