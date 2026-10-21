#catches a ValueError
try:
    x = int(input("what's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an intger")