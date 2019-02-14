name = 'World'
mood = 'good'

str = f'Hello {name}, are you {mood} ?'
# Hello World, are you good ?

str = 'Hello {}, are you {}'.format(name, mood)
# Hello World!

str = 'Hello {name}, are you {mood} ?'.format(name=name, mood=mood)
# Hello World, are you good ?

# % is very old, dont prefer it
str = "%s %s!" %("Hello", "World")
# Hello World!
