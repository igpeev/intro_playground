# TUPLE - immutable ordered sequence of arbitrary object

t = ('Norway', 3.14, 5)
print(t)
# ('Norway', 3.14, 5)

t[0]            # <-- this is how an item in a tuple can be accessed
# 'Norway'

len(t)
# 3

for item in t:
    print(item)

# Norway
# 3.14
# 5

t.count(5)      # <-- param required (how many times 5 is met in the t tuple)
#1

t.indexOf(5)    # <-- raises exeption if 5 is not in the tuple
#2

# concatenate tuples
t + ("pesho", 999)
# ('Norway', 3.14, 5, 'pesho', 999)

# repeat tuples
t * 3
# ('Norway', 3.14, 5, 'Norway', 3.14, 5, 'Norway', 3.14, 5)

# accessing nested elements
a = (55, 66), (77,88)
b = ((55, 66), (77,88))     # <-- shorthand
a[1][0]
# 77

# single member tuples
intgr = 5
intgr = (5)
e = ()  # <-- empty tuple
tpl = (5,)
type(tpl)
# <class 'tuple'>

# multiple return values ? => use tuple
def minmax(items):
    return min(items), max(items)

minmax([33, 44, 55])
# (33, 55)

# destructure a tuple ? => tuple unpacking
lower, upper = minmax([33, 44, 55])
lower
# 33
upper
# 55

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

