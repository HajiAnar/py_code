def sum(*args):
    result = 0
    for arg in args:
        if not isinstance(arg, (list, tuple)):
            result += arg
        else:
            result += sum(*arg)
    return result


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
