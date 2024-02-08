

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def find_list(struct):
    new_list = []
    for item in struct:
        if not isinstance(item, list):

            new_list.append(item)

        else:

            new_list.extend(find_list(item))


    return new_list




print(find_list(nice_list))



