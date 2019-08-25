# *args and **kwargs (any name can be used i.e. *sun and **moon)
# Good source: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/


def test_1(arg1, arg2, arg3):
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    print(f'arg3: {arg3}')


test_1('foo', 'bar', 'baz')
# arg1: foo
# arg2: bar
# arg3: baz



def test_2(*args):
    # for arg in args:                      # without 'idx'
    print(type(args))                       # <-- TUPLE !!!
    for idx, arg in enumerate(args):
        print(f'arg{idx}: {arg}')

test_2('foo', 'bar', 'baz')
# <class 'tuple'>                           # <-- !!!
# arg0: foo
# arg1: bar
# arg2: baz



def test_3(**kwargs):
    print(type(kwargs))                    # <-- DICTIONARY !!!
    for k, v in kwargs.items():
        print(f'{k}: {v}')
    some_arg = kwargs.get('name') or 'No name found'
    other_arg = kwargs.get('name1') or 'No name found'
    third_arg = kwargs.get('funky')
    print(f'some_arg: {some_arg}, other_arg: {other_arg}, third_arg: [{third_arg}]')

test_3(name='Peter', age=33)
# <class 'dict'>                           # <-- !!!
# name: Peter
# age: 33
# some_arg: Peter, other_arg: No name found, third_arg: [None]



# USING *args and **kwargs to call a function
colors = {'red', 'green', 'blue'}
data = ('two', 33, True)

def do_sth(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

do_sth(*colors)
do_sth(*data)
# blue
# red
# green
# two
# 33
# True

points = {'p1': 33, 'p2': 44, 'p3': 99}
do_sth(**points)
# 33
# 44
# 99


# using all
def some_calculation(parg, *args, **kwargs):
    my_string = parg
    my_tuple = args
    my_dictionary = kwargs

    print(my_string)
    print(str(my_tuple))
    print(str(my_dictionary))

some_calculation('Peter', 33, 44, 99, name='Stephen', age=23)
# Peter
# (33, 44, 99)
# {'name': 'Stephen', 'age': 23}


# BONUS: *args and *kwargs are convenient to forward to another func (to trace it)
def trace(f, *args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    result = f(*args, **kwargs)     # <-- forward to other func and capture the result
    print(f'result: {result}')
    return result


int('ff', base=16)                  # <-- converts base-16 int to decimal int
# 255

trace(int, 'ff', base=16)
# args: ('ff',)
# kwargs: {'base': 16}
# result: 255
# 255
