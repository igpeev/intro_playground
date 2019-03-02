# DICTIONARY - unordered key: value pairs, comma separated, keys unique (roughly javascript equivalent of object)

d = {'name': 'Peter', 'age': 33}
{'name': 'Peter', 'age': 33}

d['name']
# 'Peter'


# Make a dictionary (obj) from tuples list
person_tuples_list = [('name', 'Peter'), ('age', 33)]
d = dict(person_tuples_list)
# {'name': 'Peter', 'age': 33}

#dictionary from dict Ctor
d = dict(name='Peter', age=33)
{'name': 'Peter', 'age': 33}

# to copy a dictionary - SHALLOW !!!
new_dict = d.copy()
new_dict = dict(d)


# membership testing
'age' in d
True

'sex' in d
False


# extend a dictionary (javascript equivalent to Object.assign or {...p, ...q}
d.update({'enrolled': 999})                # { ...p, ...{ enrolled: 999 } }
new_dict = {**d, **{'enrolled': 999}}
# {'name': 'Peter', 'age': 33, 'enrolled': 999}

#shorten a dict
d.pop('enrolled')                           # <-- Error if not present
# 999

del d['enrolled']
{'name': 'Peter', 'age': 33}                # <-- Error if not present


# Iterate
for key in d:
    print('{} => {}'.format(key, d[key]))
    print('{key} => {val}'.format(key=key, val=d[key]))   # <-- same, but long-hand
# name = > Peter //  age = > 33 // enrolled = > 999

for key in d.keys():
    print(key)
# name // age  // enrolled

for val in d.values():
    print(val)
# Peter // 33 // 999

for key, val in d.items():          # returns key:val tuples list, so name the tuple vars (key, val) as you like most
    print(key, val)
    # name Peter // age 33

for key, val in enumerate(d):       # !!! note on dictionaries NOT ordered, [(name, Peter), (age, 33)]
    print(key, val)
    # 0 name // 1 age

for idx, (key, val) in enumerate(d.items()):
    # enumerate(list_of_key_val_tuples) => list_of_idx_(key_val_tuple)_tuples
    # enumerate( [(name, Peter), (age, 33)] ) => [(0, (name, Peter)), (1, (age, 33))]
    print(idx, key, val)
    # 0 name Peter // 1 age 33
