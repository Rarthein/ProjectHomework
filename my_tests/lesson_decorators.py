# def summ(a, b):
#     return a + b
#
# def example(a):
#     def inner(b):
#         print(a+b)
#     inner(3)
#
#
# if __name__ == '__main__':
#     example(2)


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(c, d): # в этот момент summ=wrapper
    return c + d


if __name__ == '__main__':
    """всё это одно и то же действие"""

    # function = logger(summ)
    # print(function(2, 3))

    # print(logger(summ)(2, 3))

    # summ = logger(summ)
    # print(summ(2, 3))

    print(summ(2, 3))
    print(summ(5, 6))
