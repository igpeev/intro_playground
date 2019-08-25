# DECORATORS - if several used, processed in reverse order (i.e. lower first, top one last)


# functions **************************************************************************
def capitalized(f):
    def wrap(*args, **kwargs):
        response = f(*args, **kwargs)
        return response.upper()

    return wrap


@capitalized
def generate_text(name):
    return f'Hello World, hello {name}'


print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER


# function CONFIGURABLE **************************************************************************
def capitalized(enabled):
    def configured_decorator(f):
        def wrap(*args, **kwargs):
            response = f(*args, **kwargs)
            return response.upper() if enabled else response
        return wrap
    return configured_decorator


@capitalized(enabled=True)
def generate_text(name):
    return f'Hello World, hello {name}'


print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER


# Classes ****************************************************************************
class Capitalized:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        result = self.f(*args, **kwargs)
        self.count += 1
        return result.upper()


@Capitalized
def generate_text(name):
    return f'Hello World, hello {name}'


print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER
print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER
print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER
print(generate_text.count)          # 3     <-- notice how .count is accessible !!!


# Class INSTANCES ****************************************************************************
# EXAMPLE with 'enabled' toggle
class Capitalized:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, f):          # <-- note the new place of 'f' injection !!!
        def wrap(*args, **kwargs):
            result = f(*args, **kwargs)
            return result.upper() if self.enabled else result
        return wrap


capitalized = Capitalized()


@capitalized
def generate_text(name):
    return f'Hello World, hello {name}'


print(generate_text('Peter'))       # HELLO WORLD, HELLO PETER
capitalized.enabled = False         # <-- note we change on the DECORATOR instance !!!
print(generate_text('Peter'))       # Hello World, hello Peter
