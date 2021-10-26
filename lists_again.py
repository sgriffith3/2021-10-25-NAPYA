cars = ["ford", "chevy", "toyota"]

fancy = ["porsche", "jaguar", "ferarri"]

old = ["911", "Model T", "Firebird"]

fancy.append(old)

cars.append(fancy)

print(cars)
# output = ['ford', 'chevy', 'toyota', ['porsche', 'jaguar', 'ferarri', ['911', 'Model T', 'Firebird']]]
# outer ds    0        1         2                                    3
# middle =                             ['porsche', 'jaguar', 'ferarri', ['911', 'Model T', 'Firebird']]
# middle ds                                0           1         2                   3
# inner =                                                               ['911', 'Model T', 'Firebird']
# inner ds                                                                 0        1           2

print("Getting to the Porsche 911")
print(cars[3])

print(cars[3][3])

print(cars[3][3][0])

# Slicing
slice_01 = cars[1:3]
print(slice_01)


