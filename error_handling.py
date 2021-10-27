
while True:
    try:
        num1 = int(input("Gimme a number: "))
        print(111 / num1)
        break
    except ValueError as err:
        print("That's not an integer, silly!")
        continue
    except ZeroDivisionError as err:
        print("Zeros are not allowed")
        continue

print("Success")
