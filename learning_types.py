# strings
"""
This is a 
multiline comment.

This doc talks
about strings.
"""

# another comment here

cat = "Garfield"
dog = 'Odie'
human = f"""
Jon was the owner 
of {cat}
and {dog}.
"""

print(cat)
print(dog)
print(human)

sent = f"{cat}'s favorite's \"food's\" is' lasagna's"
print(sent)

od = f'The dog, {dog}, is a "little slow" sometimes'
print(od.title())
print(od.capitalize())
print(od.upper())


# Integers

x = 5
print(x + 100)
print(100 - x)

print(x - 3.14)

# Float

pi = 3.14
print(pi + x)

print(type(x))
print(type(pi))
print(type(cat))



