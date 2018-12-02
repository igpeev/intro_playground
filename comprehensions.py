# Comprehensions - concise syntax for describing lists, sets or dictionary
words = 'Hello World, hello people'.split()
# ['Hello', 'World,', 'hello', 'people']

# LIST
# [ expr(item) for item in iterable ]
res = [len(word) for word in words]
# [5, 6, 5, 6]

res = []
for item in words:              # <-- long-hand
    res.append(len(item))

# SET (syntax same as list, but in curly brackets)
res = {len(word) for word in words}
# {5, 6}

# DICTIONARY
# { key_expr:value_expr for item in iterable }
res = {k: v for k, v in enumerate(words)}
# {0: 'Hello', 1: 'World,', 2: 'hello', 3: 'people'}
res_reverse_kv = {k: v for k, v in res.items()}
# {0: 'Hello', 1: 'World,', 2: 'hello', 3: 'people'}

# GENERATOR (!!! differs by round brackets)
# (expr(item) for item in iterable)
million_squares_array_now = [x*x for x in range(1000000)]

million_squares_generator = (x*x for x in range(1000000))   # <-- notice the ROUND brackets
my_list = list(million_squares_generator)                   # <-- consume


# COMPREHENSION + FILTER
# [expr(item) for item in iterable if predicate(item)]
res = [len(word) for word in words if len(word)%2 == 0]  # store only even nums
# [6, 6]

