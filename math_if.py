nums = [99, 1, 33, 63, 88, 65, 35, 236, 17]

for num in nums:
    if num < 50:
        print(f"{num} is a small number")
    elif num < 60:
        print(f"{num} still would be a failing grade")
    elif num < 70:
        print(f"{num}: D's get degrees")
    elif num < 80:
        print(f"{num}: C you in study hall")
    elif num < 90:
        print(f"{num}: not 'B'ad")
    elif num <= 100:
        print(f"{num}: you 'A'ced that!")
    else:
        print(f"{num} is a big number")
