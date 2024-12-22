def is_even(x):
    return x % 2 == 0

result_filter = list(filter(is_even, range(20)))

print(result_filter)

def double(x):
    return [x, x]

print(double(11))

result_map = list(map(double, result_filter))
print(result_map)

from itertools import chain

result_chain = list(chain(*result_map))

print(result_chain)