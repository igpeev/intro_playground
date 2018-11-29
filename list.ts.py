# List

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
