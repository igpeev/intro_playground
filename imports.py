# To import modules in REPL
# >>> import hello  # First import
# Hello World!
# >>> import hello  # Second import, which does nothing
#
# >>> import importlib
# >>> importlib.import_module('hello')          <-- here we import module name as a string
# >>> importlib.reload(hello)                   <-- NOTE we import module, NOT a string
# Hello World!
# <module 'hello' from '/home/username/hello.py'>


# To import AND run (returns dict {__name__: 'hello', __file__: 'D:\\hello.py', ...}
# >>> import runpy
# >>> runpy.run_module(mod_name='hello')        <-- by modulename
# >>> runpy.run_path(file_path='hello.py')      <-- by pathname

# Running with exec()   ... a bit out, but also works
# >>> exec(open('hello.py').read())
