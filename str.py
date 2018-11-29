# str is immutable
# >>> help(str) for more :)

# length
len('pesho')
# 5

# concatenation
# join() on separator should be called for large concats as s+= 'found' creates NEW str, str being immutble
'New' + 'found' + 'land'
# 'Newfoundland'

''.join(['New', 'found', 'land'])
# 'Newfoundland'

','.join(['New', 'found', 'land'])  # <--join string specified
# 'New,found,land'

# split
'Hello World, hello people'.split()         # when not specified, splits on space
# ['Hello', 'World,', 'hello', 'people']
'babababababa'.split('a')
# ['b', 'b', 'b', 'b', 'b', 'b', '']

# partition
'London:Edinburgh'.partition(':')
# ('London', ':', 'Edinburgh')
origin, _, destination = 'London:Edinburgh'.partition(':')  # <-- pythonic way to dump unused values, here '_'

# interpolation
'The birthday is in {0} year, {1} month and now is {1}'.format(1992, 'June')
# 'The birthday is in 1992 year, June month and now is June'

'The birthday is in {} year, {} month'.format(1992, 'June')     # <-- when used EXACTLY once
# 'The birthday is in 1992 year, June month'

'Current position is {lat} and {len}'.format(lat='3.02E', len='1.004N')     # <-- named
# 'Current position is 3.02E and 1.004N'

pos = ('3.02E', '1.004N')
'position is x={pos[0] and y={pos[1]'.format(pos=pos)           # <-- passing a tuple
# 'position is x=3.02E and y=1.004N'

import math
'Math constants: pi={m.pi}, e={m.e}'.format(m=math)
# 'Math constants: pi=3.141592653589793, e=2.718281828459045'
'Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m=math)     # <-- same but limit till the third float sign
# 'Math constants: pi=3.142, e=2.718'
