from ordered_set import OrderedSet


# noinspection PyPep8Naming
def receives_OrderedSet_int(ordered_set: 'OrderedSet[int]') -> 'OrderedSet[int]':
    return ordered_set


# MyPy should show error 'ordered_set_stubs_test.py:10: error: List item 0 has incompatible type "str"; expected "int"'
receives_OrderedSet_int(OrderedSet(['ololo']))
