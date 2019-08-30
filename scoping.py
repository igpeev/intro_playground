# LEGB = Local, Enclosing, Global, Built-in
# NOTE: inside-class, but outside-method is NOT enclosing (enclosing = in enclosing method if such)


x = 0                           # <-- visible everywhere as 'x'
print(x)                        # 0


class ShippingContainer:

    x = 33                      # <-- visible inside def as 'self.x' OR 'ShippingContainer.x'
    print(x)                    # 33

    def __init__(self):
        self.y = self.x         # 33 <-- same as ShippingContainer.x !!! (latter preferable for clarity)
        self.x = x              # 0  <-- x is the one from line 5

    def do_sth(self):
        print(self.x)           # 0 <-- this is x from line 16
        print(x)                # 0 <-- this is x from line 5
        # x = 5                 # <-- if these two lines are uncommented => ERROR on line 20 !
        # print(x)              # <-- because decl of x on line 21 is hoisted and hides x from line 5
        # print(self.y)         # 33


# from scoping import *
# 0                     # exec of line 6
# 33                    # exec of line 12

# s = ShippingContainer()
# s.do_sth()
# 0                     # exec of line 19
# 0                     # exec of line 20
# 33                    # exec of line 23
