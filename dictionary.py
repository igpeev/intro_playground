# Dictionary - unordered key: value pairs, comma separated, keys unique (roughly javascript equivalent of object)

person = {'name': 'Peter', 'age': 33}
{'name': 'Peter', 'age': 33}

person['name']
# 'Peter'

# Make a dictionary (obj) from tuples array
person_tuples_array = [('name', 'Peter'), ('age', 33)]
d = dict(person_tuples_array)
d
# {'name': 'Peter', 'age': 33}
p = dict(name='Peter', age=33)
p
{'name': 'Peter', 'age': 33}

# to copy a dictionary - SHALLOW !!!
new_dict = p.copy()
new_dict = dict(p)
new_dict.update(p)

# extend a dictionary (javascript equivalent to Object.assign or {...p, ...q}
p.update({'enrolled': True})    # { ...p, ...{ enrolled: true } }
p
# {'name': 'Peter', 'age': 33, 'enrolled': True}

# iterate
for key in p:
    print('{} => {}'.format(key, p[key]))
    # print('{key} => {val}'.format(key=key, val=p[key]))   # <-- same, but long-hand

# name = > Peter
# age = > 33
# enrolled = > True

for key in p.keys():
    print(key)
# name
# age
# enrolled

for val in p.values():
    print(val)
# Peter
# 33
# True

for key, val in p.items():      # returns key:val tuples, so name the tuple vars (key, val) as you like most
    print(key, val)

# membership testing
'age' in p
True

'sex' in p
False


del p['enrolled']
p
{'name': 'Peter', 'age': 33}

del p['enrolled']   # <-- already deleted key (or missing key) => test first !!!
# ERROR

