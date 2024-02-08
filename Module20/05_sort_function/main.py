def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))

tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))

#Вариант2
#def tpl_sort(trp_):
#    new_list = list(trp_)
#    for num in list_new:
#       if int(num) == num:
#          new_list.sort()
#          new_tuple = tuple(new_list)
#          return new_tuple
#      else:
#         return trp_
