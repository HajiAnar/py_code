

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
list3 = list(set(list1 + list2))
list3.sort()

print(*list3)

