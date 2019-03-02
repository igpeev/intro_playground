# TUPLE - immutable ordered sequence of arbitrary object
# similar to LIST, differences coming from 'immutability' of TUPLEs (no add, append, extend, remove, pop, etc.)

t = ('Norway', 3.14, True)
# ('Norway', 3.14, True)

t[0]                    # <-- ordered sequence
# 'Norway'

len(t)
# 3

t.count(3.14)            # <-- param required (how many times 5 is met in the t tuple)
# 1

t.index(3.14)            # <-- raises exeption if 5 is not in the tuple
# 2

# concatenate tuples
t + ('pesho', 999)
# ('Norway', 3.14, True, 'pesho', 999)

# repeat tuples
t * 3
# ('Norway', 3.14, True, 'Norway', 3.14, True, 'Norway', 3.14, True)

# accessing nested elements
a = (55, 66), (77, 88)
b = ((55, 66), (77, 88))  # <-- long-hand
a[1][0]
# 77

# single member tuples
intgr = 5
intgr = (5)

e = ()                    # <-- empty tuple
tpl = (5,)
type(tpl)
# <class 'tuple'>
del e                     # <-- delete tuple

# multiple return values => use tuple
def minmax(items):
    return min(items), max(items)

minmax([33, 44, 55])
# (33, 55)

# destructure a tuple => tuple unpacking
lower, upper = minmax([33, 44, 55])
lower
# 33
upper
# 55

t = (1, 2, 3)
one, two, three = t
one == 1 and two == 2 and three == 3
# True


# create tuple from other data structure ?
tuple([33, 44, 55])     # from list (array)
# (33, 44, 55)
tuple('pesho')          # from string
# ('p', 'e', 's', 'h', 'o')

# membership
5 in (3, 5, 9)
# True
5 not in (3, 5, 9)
# False


# Iterate (!!! TUPLE does NOT support .keys(), .values(), .items())
# # enumerate() yields tuples (index, value)
for item in t:
    print(item)

# Norway
# 3.14
# True

for k, v in enumerate(t):
    print(k,v)

# 0 Norway
# 1 3.14
# 2 True
