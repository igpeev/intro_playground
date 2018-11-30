# Set - unordered collection of unique, immutable objects
s = {33, 44, 55, 33}    # UNIQUE, so second 33 is dropped !!!
s
{33, 44, 55}

e = set()   # <-- to create an empty set
e = {}      # <-- creates a dictionary (obj)

s = set([3, 4, 16, 64])     # <-- from any iterable list (dict for ex)

for x in {1, 2, 7, 99}:     # <-- iterable, but order is arbitrary
    print(x)

# membership
3 in s
# True

3 not in s
# False

s.add(77)
s
{33, 44, 77, 55}

s.update([999, 888, 1001, 33])
s
# {33, 999, 1001, 44, 77, 55, 888}

s.remove(33)
s.remove(33)   # <-- ERROR if missing
# ERROR
s.discard(33)   # <-- remove OR no-error if missing

# Copy - SHALLOW !!!
j = s.copy()
j = set(s)

# UNION - in either or both sets
s.union(j)

# INTERSECTION - present in both sets
s.intersect(q)

# DIFFERENCE - not in the other ( NOT COMMUTATIVE)
s.difference(j)

# SYMMETRIC DIFFERENCE (only in one of the sets)
s.symmetric_difference(j)

# SUBSET - all elems in 1st set are present in the 2nd set (i.e. inside it)
s.issubset(j)

# DISJOINT - no elems in common
s.isdisjoint(j)

