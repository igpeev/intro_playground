# List - heterogenous mutable sequence
s = 'hello world hello people'.split()
s
# ['hello', 'world', 'hello', 'people']
s[1]
# 'world'
s[-3]
# 'world'

#slice
s[1:3]
# ['world', 'hello']

s[1:]           # <-- till the end
# ['world', 'hello', 'people']

s[:1]           # <-- till (but NOT including) 1
# ['hello']

# FULL SLICE (full copy), SHALLOW !!!
full_slice = s[:]
full_slice = s.copy()   # <-- same, more readable
full_slice = list(s)    # <-- same via list Ctor
full_slice is s
# False
full_slice == s
# True

#enumerate() yields tuples (index, value)
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

# Repeat list using * operator
l = [5, 10, 33]
s = l * 3
s
# [5, 10, 33, 5, 10, 33, 5, 10, 33]

w = 'hello world hello people'.split()
w
# ['hello', 'world', 'hello', 'people']
i = w.index('world')
i
# 0
w.index('planet')
# ERROR !!!

w.count('hello')
# 2

'hello' in w
# True

'hello' not in w
# False

del w[1]            # <-- remove an item by POSITION (splice)
# ['hello', 'hello', 'people']

w.remove('people')  # <-- remove by VALUE
# ['hello', 'hello']

w.insert(2, 'wrold')
# ['hello', 'hello', 'wrold']

' '.join(w)
# 'hello hello wrold'

# concat lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
# [1, 2, 3, 4, 5, 6]

l3.extend([-5, -6, -7])
# [1, 2, 3, 4, 5, 6, -5, -6, -7]

l3.sort()
l3
[-7, -6, -5, 1, 2, 3, 4, 5, 6]

l3.sort(reverse=True)
l3.reverse()            # <-- same reverse, more explicit

w = 'hi my name is sam'.split()
w.sort(key=len)
w
['hi', 'my', 'is', 'sam', 'name']

i = [19, 10, 33]
new_sorted_list = sorted(i)
new_sorted_list
# [10, 19, 33]
new_sorted_list_2 = reversed(i)
new_sorted_list_2
# <list_reverseiterator object at 0x00000271ED149EF0>   # <-- !!!
res = list(new_sorted_list_2)
# [33, 10, 19]
