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

result_vowels = print(list(x for x in "hello" if x in ['a', 'e', 'i', 'o', 'u']))

'''4'''

num = range(50)
result_arithmetic = list(filter(lambda x: x % 3 ==0 or x% 5 == 0, num))
av_arithmetic = sum(result_arithmetic) / len(result_arithmetic)
print(round(av_arithmetic))

'''5'''

from itertools import chain

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

join_list = list(set(chain(list1, list2, list3)))
print(join_list)

'''6'''

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

filtered_people = list(filter(lambda x: x["age"] == 30, people))
print(filtered_people)