# Dictionary

# Syntax:    {key: value}

pets = {"dog": "mudge", "fish": "dorothy"}
print(pets)
print(type(pets))

print(pets["dog"])

new_dog = "fido"
pets["dog"] = ["mudge", new_dog]

print(pets)
print(pets["dog"])
print(pets["dog"][1])

print(pets.get("snorfy"))


print(pets.keys())
print(pets.values())
print(pets.items())
