# SET - unordered collection of unique, immutable objects
s = {33, 44, 55, 33}    # UNIQUE, so second 33 is dropped !!!
# {33, 44, 55}

s = set()   # <-- to create an empty set
d = {}      # <-- creates a dictionary (obj)

s = set([3, 4, 16, 64])     # <-- from any iterable list (dict for ex)


# membership
3 in s
# True

3 not in s
# False


# Copy - SHALLOW !!!
j = s.copy()
j = set(s)


s.add(77)                   # {33, 44, 77, 55}
s.update([999, 888, 33])    # {33, 999, 1001, 44, 77, 55, 888}
s.remove(33)
s.remove(33)                # <-- ERROR if missing
s.discard(33)               # <-- remove OR no-error if missing
s.pop()                     # <-- !!! takes out a RANDOM element (set is unordered), hence takes NO args
#99
s.clear()                   # empty a set
del s                       # delete completely


# Iterate
for x in {1, 2, 7, 99}:     # <-- iterable, but order is arbitrary
    print(x)
# 1 // 2 // 99 // 7


# SET specific operations
# All have an _update() variant, that changes the first set by removing the matching items (instead of returning them)
s1 = {33, 18, 22}
s2 = {11, 22, 33, 99}

# UNION - in either or both sets
s.union(j)
# {33, 18, 99, 22, 11}

# INTERSECTION - present in both sets
s1.intersection(s2)
# {33, 22}

# DIFFERENCE - not in the other ( NOT COMMUTATIVE)
s1.difference(s2)
# {18}
s2.difference(s1)
# {11, 99}

# SYMMETRIC DIFFERENCE (only in one of the sets)
s1.symmetric_difference(s2)
# {99, 11, 18}


# BOOLEAN - all elems in 1st set are present in the 2nd set (i.e. inside it)
s.issubset(j)
# False

# BOOLEAN - no elems in common
s.isdisjoint(j)
# False