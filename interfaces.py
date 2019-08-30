# Python is dynamic typed and has no concept of interfaces
# Ducktyping = if sth quacks like a duck, swims like a duck => it's a duck
# HOWEVER, one can implement the concept of interfaces via the use of ABC (Abstract Base Class)

from abc import ABC, abstractmethod


class AbstractIDE(ABC):

    @abstractmethod
    def execute(self):
        pass


class PyCharm(AbstractIDE):

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class SimpleIde(AbstractIDE):

    def execute(self):
        print('Compiling')
        print('Running')


class Laptop:

    def code(self, ide):
        ide.execute()


# from interfaces import *
# p = PyCharm()
# s = SimpleIde()
# l = Laptop()

# l.code(p)
# Spell Check
# Convention Check
# Compiling
# Running

# l.code(s)
# Compiling
# Running
