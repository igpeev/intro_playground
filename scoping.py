# LEGB = Local, Enclosing, Global, Built-in
# NOTE: inside-class, but outside-method is NOT enclosing (enclosing = in enclosing method if such)


x = 0
print(x)


class ShippingContainer:

    x = 33
    print(x)

    def __init__(self):
        self.x = x

    def do_sth(self):
        print(self.x)
        print(x)
        # x = 5                 # <-- if these two lines are uncommented => ERROR on line 19 !
        # print(x)              # <-- because decl of x on line 20 is hoisted and hides x from line 5


# from scoping import *
# 0                     # line 6
# 33                    # line 12

# s = ShippingContainer()
# s.do_sth()
# 0                     # line 18
# 0                     # line 19
