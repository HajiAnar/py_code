def support_func(argument):

    sup_elem = argument[-1]
    left_border = []
    middle_border = []
    right_border = []
    for element in argument:
        if element < sup_elem:
            left_border.append(element)
        elif element == sup_elem:
            middle_border.append(element)
        else:
            right_border.append(element)

    result = left_border, middle_border, right_border
    return result


def quick_sort(argument):

    if len(argument) <= 1:

        return argument

    left_border, middle_border, right_border = support_func(argument)

    return quick_sort(left_border) + middle_border + quick_sort(right_border)

x = [4, 9, 2, 7, 5]

print(quick_sort(x))