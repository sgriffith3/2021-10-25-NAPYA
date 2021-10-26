# Grocery List
# - bread:
#     quantity: 2
#     type: gluten free
# - butter
# - milk
# - eggs

groceries = []
groceries.append("bread")
print(groceries)

groceries.append("butter")
groceries.append("milk")
groceries.append("eggs")
print(groceries)

wife_wants = ["ketchup", "flax seeds", "tennis shoes"]
print(wife_wants)

#groceries.append(wife_wants)
groceries.extend(wife_wants)
print(groceries)

groceries.sort()
print(groceries)


print("\n\n\n BREAK \n\n\n")

cars = ["F150", "Lambo", "Prius"]
#index    0        1        2
#rev     -3       -2       -1


print(cars)
print(cars[0])
print(cars[-3])

print(cars[1])
print(cars[-2])

print(cars[2])
print(cars[-1])

# I think a Lambo would be fun, and a F150 would be useful, but a Prius is neat too

print(f"I think a {cars[1]} would be fun, and a {cars[0]} would be useful, but a {cars[2]} is neat too")

