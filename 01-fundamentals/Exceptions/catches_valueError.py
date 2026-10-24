#catches a ValueError
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an intger")

print(f"x is {x}")

#Demonstrate else
try:
    x= int(input("what's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#adds a loop
while True:
    try:
        x = int(input("what's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")