# Generators are single-use objects, that can do the following:


def gen123():
    yield 1
    yield 2
    yield 3
    # return # <-- there's an implicit 'return' in the end of the definition


my_gen = gen123()
next(my_gen)        # <-- effectively my_gen python iterator
# 1
# next(my_gen)
# 2
# next(my_gen)
# 3

# Because generators are iterators => can be used in any Python construct that expects iterators, e.g.:
for my_num in gen123():
    print(my_num)
# 1
# 2
# 3

for i in range(20, 30, 3):
    print(i)
# 20
# 23
# 26
# 29
