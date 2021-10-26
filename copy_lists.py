# Take the following lists

dogs = ["fido", "spot", "lucky"]

cats = ["fluffy", "snowball", "garfield"]

# And combine them into a list called pets.
pets = dogs.copy()
pets.extend(cats)

print("Pets")
print(pets)
print("cats")
print(cats)
print("dogs")
print(dogs)

dogs.append("woof woof")
print(dogs)

print(pets)
print(id(pets))
print(id(dogs))
print(id(cats))

my_pets = {'dogs': dogs.copy()}
print(f"My Pets: {my_pets}")

dogs.append("ruff")
print(f"My Pets: {my_pets}")

your_dogs = my_pets.copy()
print(id(your_dogs))
print(id(my_pets))

print(your_dogs)

my_pets["cats"] = cats
print(your_dogs)


