numbers_file = open('numbers.txt', 'r')
str_list = numbers_file.read().split()
numbers_file.close()

numb_list = [int(i_elem) for i_elem in str_list]

summa = 0

for i_numb in numb_list:
    summa += i_numb


print('Сумма чисел в файле numbers.txt равна', summa)
