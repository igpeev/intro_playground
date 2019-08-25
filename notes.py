def some_func():
    a = 33

    # built-in func returns a dict mapping local var names to their values
    print(locals())


some_func()     # {'a': 33}


# in __init__.py (which is executed when module is loaded)
# one can specify what should be imported when 'from reader.compressed import *' is used
# from reader.compressed.q import opener as QQQ_opener  # <-- q.py
# from reader.compressed.z import opener as ZZZ_opener  # <-- z.py
# __all__ = ['QQQ_opener', 'ZZZ_opener']

