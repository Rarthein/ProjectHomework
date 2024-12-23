# def is_even(x):
#     return x % 2 == 0
#
# result_filter = list(filter(is_even, range(20)))
#
# print(result_filter)
#
# def double(x):
#     return [x, x]
#
# print(double(11))
#
# result_map = list(map(double, result_filter))
# print(result_map)
#
# from itertools import chain
#
# result_chain = list(chain(*result_map))
#
# print(result_chain)

'''1'''

result_cubed = print(list(x ** 3 for x in range(11) if x % 2 == 0))

'''2'''

num_list = [2, 3, -5, 8, -4, 1, 0, -10, 12]


def sum_positive(num_list):
    return sum(x ** 2 for x in num_list if x > 0)

print(sum_positive(num_list))

'''3'''

