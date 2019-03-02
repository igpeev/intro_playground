# List - heterogenous mutable sequence
l = 'hello world hello people'.split()
# ['hello', 'world', 'hello', 'people']

l[1]
# 'world'

l[-3]
# 'world'

#slice
l[1:3]
# ['world', 'hello']

l[1:]           # <-- till the end
# ['world', 'hello', 'people']

l[:1]           # <-- till (but NOT including) 1
# ['hello']


idx = l.index('world')
# 0

idx = l.index('planet')
# ERROR !!!

l.count('hello')
# 2


# membership testing
'hello' in l
# True

'hello' not in l
# False


# FULL SLICE (full copy), SHALLOW !!!
full_slice = l[:]
full_slice = l.copy()   # <-- same, more readable
full_slice = list(l)    # <-- same via list Ctor

full_slice is l         # not same object
# False
full_slice == l         # same content (incl. same order)
# True


# remove item from list
l.pop(2)                # <-- remove item by POSITION (returns the removed item)
# world

del l[1]                # <-- remove item by POSITION (splice)
# None

l.remove('people')      # <-- remove item by VALUE
# None

l.insert(2, 'pears')    # ['hello', 'world,', 'pears', 'hello', 'people']
# None

# concat lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
# [1, 2, 3, 4, 5, 6]

# Repeat list using * operator
s = l * 3                       # [1, 2, 3, 1, 2, 3, 1, 2, 3]

l3.extend([-5, -6, -7])         # [1, 2, 3, 4, 5, 6, -5, -6, -7]
# None

l1.append(['pears', 'apples'])  # <-- takes exactly 1 arg, [1, 2, 3, ['pears', 'apples]]
# None

'_'.join(l)
# hello_world,_hello_people


# Iterate (!!! list does NOT support .keys(), .values(), .items())
# enumerate() yields tuples (index, value)
t = [100, 200, 300]
for p in enumerate(t):
    print(p)

# (0, 100)
# (1, 200)
# (2, 300)

for idx, val in enumerate(t):   # <-- with tuple unpacking (idx, val - or whatever naming is liked)
    print(idx, val)
# 0 100
# 1 200
# 2 300


# Sorting
l3.sort()                       # [-7, -6, -5, 1, 2, 3, 4, 5, 6]

l3.sort(reverse=True)
l3.reverse()                    # <-- same reverse, more explicit


l1 = 'hi my name is sam'.split()
l1.sort(key=len)
['hi', 'my', 'is', 'sam', 'name']

l2 = [19, 10, 33]
new_sorted_list = sorted(l2)    # <-- i2 stays [19, 10, 33]
# [10, 19, 33]

new_reversed_list_2 = reversed(l2)
res = list(new_reversed_list_2)
# [33, 10, 19]

# sort list of dictionaries
l = [{'name': 'John', 'age': 33}, {'name': 'Peter', 'age': 20}, {'name': 'Rick', 'age': 42}]
sorted(l, key = lambda person: person['age'])
# [{'name': 'Peter', 'age': 20}, {'name': 'John', 'age': 33}, {'name': 'Rick', 'age': 42}]
