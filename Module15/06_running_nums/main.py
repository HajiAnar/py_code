


n = int(input("Кол-во элементов: "))
start_list = []


for _ in range(n):
    element = input("Введите элемент списка: ")
    start_list.append(element)

k = int(input("Сдвиг: "))
index = 0
while index < n - 1:
    empty_place = start_list[index]
    start_list[index] = start_list[index - k]
    start_list[index - k] = empty_place
    index += 1

print(start_list)