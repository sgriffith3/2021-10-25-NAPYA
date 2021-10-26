# Part 1

# Take the following lists

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

# And combine them into a list called pets.
pets = cats + dogs
print(pets)

pets_02 = []
pets_02.extend(cats)
pets_02.extend(dogs)
print(pets_02)


# Part 2

# Using the same lists from above,
# create a dictionary called my_pets
# that has the keys of 'dogs' and 'cats'
# with the values being the appropriate
# lists.

my_pets = {'dogs': dogs, 'cats': cats}
print(my_pets)

# Part 3

# Prove you can use the pets list to print
# "I only own spot and snowball"
txt = f"I only own {pets[4]} and {pets[1]}"
print(txt)

# Part 4

# Prove you can use the my_pets dict to print
# "I want to adopt fido and garfield too" 
txt2 = f"I want to adopt {my_pets['dogs'][0]} and {my_pets['cats'][-1]} too"
print(txt2)
